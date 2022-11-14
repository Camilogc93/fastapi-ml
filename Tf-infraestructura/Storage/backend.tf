terraform {
backend "gcs" {
  bucket = "tf-data"   # GCS bucket name to store terraform tfstate
  prefix = "test-mlops"           # Update to desired prefix name. Prefix name should be unique for each Terraform project having same remote state bucket.
  }
}