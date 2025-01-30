from typing import List

import uvicorn
from botocore.exceptions import ClientError
from fastapi import FastAPI, UploadFile, File, HTTPException
from starlette.middleware.cors import CORSMiddleware

from r2 import return_admin_r2_client, return_readonly_r2_client
from share import upload_file_name_formatter, return_env_value

ALLOWED_IMAGE_TYPES: List[str] = ['image/jpeg', 'image/png', 'image/webp']
ORIGINS = [
	"localhost:3000",
	"http://localhost:3000",
	"https://dns.jeongmingz.life",
	]


app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=ORIGINS,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
	)


@app.get("/")
async def root():
	return {"message": "Hello World"}


@app.post("/api/v1/resume/clipboard_upload")
async def clipboard_upload(
		file: UploadFile = File(...)
		):

	if file.content_type not in ALLOWED_IMAGE_TYPES :
		raise HTTPException(status_code=400, detail="Invalid file type")


	admin_r2 = return_admin_r2_client()
	bucket_name = return_env_value("CLOUDFLARE_R2_BUCKET_NAME")

	try:
		object_name = f"images/{upload_file_name_formatter()}"
		admin_r2.upload_fileobj(file.file, bucket_name, object_name,
		                  ExtraArgs={'ContentType': file.content_type})

		return {"url": f"{return_env_value('CLOUDFLARE_R2_PUBLIC_URL')}/{object_name}"}
	except ClientError as e:
		raise HTTPException(status_code=500, detail="File upload failed")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)