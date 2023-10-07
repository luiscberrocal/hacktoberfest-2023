clean: ## remove build artifacts
	rm -fr kaggle/products
	rm -rf kaggle/data
run:
	ploomber build
