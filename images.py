import os
import re
import shutil

# Paths
posts_dir = "/Users/arnaudlarrieu/Documents/batnano/content/posts/"
attachments_dir = "/Users/arnaudlarrieu/Library/Mobile Documents/iCloud~md~obsidian/Documents/posts/posts/"
static_images_dir = "/Users/arnaudlarrieu/Documents/batnano/static/images/"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r") as file:
            content = file.read()
        
        # Step 2: Find all image links for .png, .jpg, and .jpeg extensions
        images = re.findall(r'\[\[([^]]*\.(?:png|jpg|jpeg))\]\]', content, re.IGNORECASE)
        print(f"Found images in {filename}: {images}")
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown link without an exclamation mark and replace spaces with %20
            markdown_image = f"[Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)
            else:
                print(f"Image not found: {image_source}")

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")