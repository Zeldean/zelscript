"""Image resizer - resize image to target dimensions while preserving aspect ratio"""
import sys
from PIL import Image

def get_image_size(image_path):
    """Get the pixel dimensions of an image"""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        print(f"Error opening image: {e}")
        return None, None

def get_scale_factor(orig_width, orig_height, target_width=600, target_height=200):
    """Calculate the scaling factor to fit image within target dimensions"""
    f_width = target_width / orig_width
    f_height = target_height / orig_height
    f_small = min(f_width, f_height)
    
    new_width = int(orig_width * f_small)
    new_height = int(orig_height * f_small)
    
    return f_small, new_width, new_height

def get_background_color(image_path, border_size=10):
    """Get most common color from 10-pixel border around image perimeter"""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            border_pixels = []
            
            # Top and bottom borders (full width)
            for y in range(min(border_size, height)):
                for x in range(width):
                    border_pixels.append(img.getpixel((x, y)))
                    if y < height - border_size:
                        border_pixels.append(img.getpixel((x, height - 1 - y)))
            
            # Left and right borders (excluding corners already captured)
            for x in range(min(border_size, width)):
                for y in range(border_size, height - border_size):
                    border_pixels.append(img.getpixel((x, y)))
                    if x < width - border_size:
                        border_pixels.append(img.getpixel((width - 1 - x, y)))
            
            # Find most common color
            from collections import Counter
            most_common = Counter(border_pixels).most_common(1)[0][0]
            return most_common
            
    except Exception as e:
        print(f"Error getting background color: {e}")
        return (255, 255, 255)  # Default to white

def scale_image(image_path, scale_factor):
    """Scale image by given factor"""
    try:
        with Image.open(image_path) as img:
            new_width = int(img.width * scale_factor)
            new_height = int(img.height * scale_factor)
            scaled_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            return scaled_img
    except Exception as e:
        print(f"Error scaling image: {e}")
        return None

def ratio_adjust(scaled_img, target_width=600, target_height=200, bg_color=(255, 255, 255)):
    """Center scaled image on target canvas with background color"""
    try:
        # Create new canvas with target size and background color
        canvas = Image.new('RGB', (target_width, target_height), bg_color)
        
        # Calculate centering position
        x_offset = (target_width - scaled_img.width) // 2
        y_offset = (target_height - scaled_img.height) // 2
        
        # Paste scaled image onto canvas
        canvas.paste(scaled_img, (x_offset, y_offset))
        return canvas
    except Exception as e:
        print(f"Error adjusting ratio: {e}")
        return None

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python img_resize.py <input_path> [output_path]")
        sys.exit(1)
    
    input_path = sys.argv[1]
    if len(sys.argv) == 3:
        output_path = sys.argv[2]
    else:
        import os
        name, ext = os.path.splitext(input_path)
        output_path = f"{name}_resized{ext}"
    
    width, height = get_image_size(input_path)
    if not width or not height:
        sys.exit(1)
    
    f_small, new_width, new_height = get_scale_factor(width, height)
    bg_color = get_background_color(input_path)
    
    scaled_img = scale_image(input_path, f_small)
    if not scaled_img:
        sys.exit(1)
    
    final_img = ratio_adjust(scaled_img, bg_color=bg_color)
    if not final_img:
        sys.exit(1)
    
    final_img.save(output_path)
    print(f"Resized image saved to: {output_path}")

if __name__ == "__main__":
    main()