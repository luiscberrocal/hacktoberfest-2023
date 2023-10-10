clean: ## remove build artifacts
	rm -fr src/products
	rm -rf src/data
r:
	ploomber build

run:
	ploomber build --entry-point ./house_pricing/pipeline.h2.yaml

