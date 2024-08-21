from flask import Blueprint, jsonify, request
from models import Country, CountryNeighbour
from db import db

def init_routes(app):
    api_bp = Blueprint('api', __name__)

    @api_bp.route('/country', methods=['GET'])
    def get_all_countries():
        sort_by = request.args.get('sort_by', 'a_to_z')
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 20))
        name = request.args.get('name', None)
        region = request.args.get('region', None)
        subregion = request.args.get('subregion', None)

        query = Country.query

        if name:
            query = query.filter(Country.name.ilike(f'%{name}%'))
        if region:
            query = query.filter_by(region=region)
        if subregion:
            query = query.filter_by(subregion=subregion)
        
        print(f"Sort by: {sort_by}")
        
        if sort_by == 'a_to_z':
            query = query.order_by(Country.name.asc())
        elif sort_by == 'z_to_a':
            query = query.order_by(Country.name.desc())
        elif sort_by == 'population_high_to_low':
            query = query.order_by(Country.population.desc())
        elif sort_by == 'population_low_to_high':
            query = query.order_by(Country.population.asc())
        elif sort_by == 'area_high_to_low':
            query = query.order_by(Country.area.desc())
        elif sort_by == 'area_low_to_high':
            query = query.order_by(Country.area.asc())
        print(str(query))
        paginated_countries = query.paginate(page=page, per_page=limit, error_out=False)

        countries_list = [{
            "id": country.id,
            "name": country.name,
            "cca3": country.cca3,
            "currency_code": country.currency_code,
            "currency": country.currency,
            "capital": country.capital,
            "region": country.region,
            "subregion": country.subregion,
            "area": country.area,
            "map_url": country.map_url,
            "population": country.population,
            "flag_url": country.flag_url
        } for country in paginated_countries.items]

        return jsonify({
            "message": "Country list",
            "data": {
                "list": countries_list,
                "has_next": paginated_countries.has_next,
                "has_prev": paginated_countries.has_prev,
                "page": paginated_countries.page,
                "pages": paginated_countries.pages,
                "per_page": paginated_countries.per_page,
                "total": paginated_countries.total
            }
        }), 200

    @api_bp.route('/country/<int:id>', methods=['GET'])
    def get_country_by_id(id):
        country = Country.query.get(id)
        if not country:
            return jsonify({"message": "Country not found", "data": {}}), 404

        country_data = {
            "id": country.id,
            "name": country.name,
            "cca3": country.cca3,
            "currency_code": country.currency_code,
            "currency": country.currency,
            "capital": country.capital,
            "region": country.region,
            "subregion": country.subregion,
            "area": country.area,
            "map_url": country.map_url,
            "population": country.population,
            "flag_url": country.flag_url
        }

        return jsonify({"message": "Country detail", "data": {"country": country_data}}), 200

    @api_bp.route('/country/<int:id>/neighbour', methods=['GET'])
    def get_country_neighbours(id):
        country = Country.query.get(id)
        if not country:
            return jsonify({"message": "Country not found", "data": {}}), 404

        neighbours = CountryNeighbour.query.filter_by(country_id=id).all()
        neighbours_list = []
        for neighbour in neighbours:
            neighbour_country = Country.query.get(neighbour.neighbour_country_id)
            if neighbour_country:
                neighbours_list.append({
                    "id": neighbour_country.id,
                    "name": neighbour_country.name,
                    "cca3": neighbour_country.cca3,
                    "currency_code": neighbour_country.currency_code,
                    "currency": neighbour_country.currency,
                    "capital": neighbour_country.capital,
                    "region": neighbour_country.region,
                    "subregion": neighbour_country.subregion,
                    "area": neighbour_country.area,
                    "map_url": neighbour_country.map_url,
                    "population": neighbour_country.population,
                    "flag_url": neighbour_country.flag_url
                })

        return jsonify({"message": "Country neighbours", "data": {"countries": neighbours_list}}), 200

    app.register_blueprint(api_bp)
