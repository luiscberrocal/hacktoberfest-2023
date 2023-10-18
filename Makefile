clean: ## remove build artifacts
	rm -fr src/products
	rm -rf src/data
run:
	ploomber build

r:
	ploomber build --entry-point ./src/pipeline.h2.yaml

