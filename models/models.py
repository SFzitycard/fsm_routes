# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta

class RoutesWizard(models.TransientModel):
    _name = 'fms.routeswizard'

    name = fields.Char(string='Create route')
    description = fields.Text(string='Create a route of the selected tasks')
    
    final_route=""
    def create_route(self):
        coordinates=""
        link="https://www.google.com/maps/dir"
        # Calculate the route coordinates, be sure that the locations used for the clients have a computed latitude and longitude
        # Has a high error margin because the compute function of the FSM doesn't work exactly as intended.

        #fms_orders = self.env.context.get('active_ids', [])
        #for order in fms_orders:
        #    latitude = order.location_id.partner_latitude
        #    longitude = order.location_id.partner_longitude
        #    coordinates=coordinates+"/latitude,longitude"
        #final_route=link+coordinates

        # Calculate the route coordinates, be sure that the locations have at least the Street, Zip Code and City
                            
        fms_orders = self.env.context.get('active_ids', [])
        for order in fms_orders:
            street = order.location_id.street
            street2 = order.location_id.street2
            city = order.location_id.city
            state_id = order.location_id.state_id
            zip = order.location_id.zip
            country = order.location_id.country_id
            coordinates=coordinates+"/street,zip,city"

        final_route=link+coordinates


        # Return a message indicating the creation of the route
        return {
            'name': 'Route Created',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'description': final_route,
            'target': 'current',
        }
