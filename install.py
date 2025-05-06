import kagglehub

# Download latest version
path = kagglehub.dataset_download("quandang/vietnamese-foods")

print("Path to dataset files:", path)