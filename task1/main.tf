
resource "aws_s3_bucket" "bucket1" {
  bucket = "manasbucket726"
  
  tags = {
    name = "s3_bucket"
  }
}

resource "aws_s3_object" "dir1" {
  bucket = aws_s3_bucket.bucket1.bucket
  key    = "dir1/"

  depends_on = [aws_s3_bucket.bucket1]
}

resource "aws_s3_object" "dir2" {
  bucket = aws_s3_bucket.bucket1.bucket
  key    = "dir2/"

  depends_on = [aws_s3_bucket.bucket1]
}

resource "aws_s3_bucket" "output_task2_bucket" {
  bucket = "manasbucket789"
  
  tags = {
    name = "s3_bucket"
  }
}