aggregate.json:
	mapshaper aggregate.csv \
	  -points x=longitude y=latitude \
	  -o format=geojson
