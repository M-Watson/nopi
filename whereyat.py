import requests


url_1 = "https://gis.nola.gov/arcgis/rest/services/CompositePIN2/GeocodeServer/findAddressCandidates?SingleLine={}&f=json".format(address)


url_2 = "https://gis.nola.gov/arcgis/rest/services/apps/WhereYat/MapServer/identify?
            geometry={x:{XVAL},y:{YVAL}}&
            geometryType=esriGeometryPoint&
            layers=all&
            tolerance=2&
            mapExtent=num,num,num,num&
            imageDisplay=20,20,96&
            returnGeometry=false&
            f=json"
