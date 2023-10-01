clean: ## remove build artifacts
	rm -fr kaggle/products
run: clean
	ploomber build
