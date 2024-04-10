from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

# Connect to SharePoint
ctx = ClientContext("https://your-sharepoint-site.sharepoint.com/sites/your-site").with_credentials(UserCredential("username", "password"))

# Open the CSV file and read its content
with open("path/to/your/csv/file.csv", "rb") as content_file:
    file_content = content_file.read()

# Set the destination path for the file to be uploaded
destination_url = "/sites/your-site/Shared Documents/path/to/destination/folder/file.csv"

# Upload the file to SharePoint
ctx.web.get_folder_by_server_relative_url("/sites/your-site/Shared Documents/path/to/destination/folder").upload_file(destination_url, file_content)