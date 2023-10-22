clean: ## remove build artifacts
	rm -fr src/products
	rm -rf src/data
run:
	ploomber build

