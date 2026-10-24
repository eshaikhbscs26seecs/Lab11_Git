# Storage Estimator
# Convert GB into MB and display both values

size_gb = float(input("Enter storage size in GB: "))

size_mb = size_gb * 1024

size_kb = size_mb * 1024

print("Storage size in GB:", size_gb)
print("Storage size in MB:", size_mb)
print("Storage size in KB:", size_kb)