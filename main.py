from PIL import Image
import os

def resize_images_in_directory(directory, max_width=1024):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                with Image.open(file_path) as img:
                    # Calculate the new height maintaining the aspect ratio
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)

                    # Resize the image
                    img_resized = img.resize((max_width, new_height), Image.ANTIALIAS)

                    # Save the resized image
                    img_resized.save(file_path)


print("処理開始")
directory = "./imagefile"
resize_images_in_directory(directory)
print("処理終了：画像ファイルをresizeして、上書き保存しました。")
