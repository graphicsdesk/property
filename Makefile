aggregate.svg:
	mapshaper aggregate.csv \
	  -points x=longitude y=latitude \
		-style r=4 \
	  -o format=svg
