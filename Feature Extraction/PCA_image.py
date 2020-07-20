#A pipeline with a scaler and PCA model to select 78 components 
#has been pre-loaded for you as pipe. This pipeline has already
#been fitted to the entire MNIST dataset except for the 16 samples in X_test.

plot_digits(X_test)

# Transform the input data to principal components
pc = pipe.transform(X_test)

# Prints the number of features per dataset
print("X_test has {} features".format(X_test.shape[1]))
print("pc has {} features".format(pc.shape[1]))

# Transform the input data to principal components
pc = pipe.transform(X_test)

# Inverse transform the components to original feature space
X_rebuilt = pipe.inverse_transform(pc)

# Plot the reconstructed data
plot_digits(X_rebuilt)
