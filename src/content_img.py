# Content for the image tools. build.py registers each entry with tool(...).
# extra: sections added below the intro/how-to/why text. faq: (question, answer) pairs, also used for FAQ schema.
I = {

"image-resizer": dict(
name="Image Resizer",
title="Image Resizer: Resize Photos by Pixels or Percent Online | VipTools",
desc="Resize images to exact pixels or a percentage in your browser. Keep the aspect ratio, export JPG, PNG or WebP. Free and private.",
extra=[
 ("Common image sizes", [
  "Many platforms set fixed image sizes. Profile photos are often 400 x 400 pixels, YouTube thumbnails are 1280 x 720, Instagram square posts are 1080 x 1080, and website banners are commonly 1500 x 500. Entering the exact size makes your picture fit without the platform cropping parts of it or stretching it.",
  "When a size is not listed, pick the closest width and keep the aspect ratio ticked. Keeping the ratio stops the image from looking squashed or stretched."]),
 ("Pixels or percentage", [
  "Use pixels when a site or form gives a required size. Use percentage when you simply want a smaller copy, for example 50 percent for a quick preview or 25 percent for a thumbnail. The percentage option calculates both width and height from the original image so the proportions stay correct.",
  "Enlarging works too, but a small picture cannot gain real detail. Scaling it up to 200 percent makes it bigger and softer, so start with the largest version you have when you need a large output."]),
 ("Choosing the output format", [
  "JPG gives the smallest files for photographs and is accepted almost everywhere. PNG keeps sharp edges and transparent backgrounds, which suits logos, screenshots and icons, but PNG files are larger for photos. WebP is a modern format that is usually smaller than JPG at the same visual quality and is a good choice for websites.",
  "When you export a transparent image as JPG, the tool fills the transparent areas with white, because JPG cannot store transparency."]),
 ("Resizing for a website", [
  "Page speed affects both visitors and search rankings. Resizing an image to the size it is shown on the page, instead of uploading a 5000-pixel camera photo and hiding it with CSS, reduces download time. As a rule, keep most web photos under 2000 pixels on the longest side and under a few hundred kilobytes.",
  "Combine resizing with compression for the best result. Resize first to the display size, then compress or export as WebP to shrink the file further."])
],
faq=[
 ("Is my photo uploaded when I resize it?", "No. The image is loaded and redrawn inside your browser. The file never leaves your device."),
 ("Why did my resized image look blurry?", "Enlarging a small image cannot add detail. Shrinking keeps sharpness. Start from the largest original you have."),
 ("What does keeping the aspect ratio mean?", "It means the height changes in the same proportion as the width, so the picture is not stretched or squashed. Turn it off only if you deliberately want a different shape."),
 ("Why is the JPG background white?", "JPG has no transparency, so transparent areas are filled with white. Use PNG or WebP to keep transparency."),
 ("Is there a size limit?", "Very large images, above about 10000 pixels on one side, are blocked. Most phones and laptops handle images well within the limit.")
]),

"image-format-converter": dict(
name="Image Format Converter",
title="Image Format Converter: JPG, PNG and WebP Online | VipTools",
desc="Convert images between JPG, PNG and WebP in your browser. Choose quality, keep transparency where supported. Free, fast and private.",
extra=[
 ("JPG, PNG or WebP: which is best", [
  "JPG is the most widely accepted format for photographs. It compresses detailed pictures well but cannot show transparency and loses a little quality each time it is saved again.",
  "PNG is lossless, which means no quality is lost, and it supports transparent backgrounds. The trade-off is file size: photos saved as PNG are often several times larger than JPG.",
  "WebP is a newer format from Google. At similar quality it is usually smaller than JPG and PNG, supports transparency and is supported by all current major browsers. Many image-heavy sites now serve WebP for faster loading."]),
 ("What quality setting means", [
  "For JPG and WebP, quality controls the balance between file size and detail. Values from 80 to 90 are visually close to the original for most photos. Lower values shrink the file more but add visible artefacts, such as blocky edges around text or colours that look blotchy.",
  "The quality setting is not used for PNG because PNG is lossless. The slider is disabled when PNG is selected."]),
 ("Converting screenshots and logos", [
  "Screenshots and logos with flat colours usually look best as PNG, because compression methods made for photos can blur sharp text and lines. If the file is too big for a website, try WebP at quality 90 before choosing JPG."]),
 ("Why conversion matters for websites", [
  "Modern file formats reduce download times, which helps visitors on slow mobile connections and supports better page performance scores. Converting an existing JPG or PNG to WebP is one of the simplest ways to lighten a site without changing how it looks.",
  "Check the converted file in the context where you will use it. If a platform rejects WebP, export a JPG copy instead."])
],
faq=[
 ("Is my image uploaded during conversion?", "No. The conversion runs in your browser, so the original file stays on your device."),
 ("Does converting to JPG reduce quality?", "JPG is a lossy format, so some detail is removed. Use a higher quality setting, such as 90, to keep the picture close to the original."),
 ("Why does the PNG file get bigger?", "PNG is lossless and stores every pixel exactly. Photos converted from JPG to PNG become larger without gaining any quality."),
 ("Which format keeps transparency?", "PNG and WebP keep transparent backgrounds. JPG does not, so transparent areas turn white."),
 ("Can I convert HEIC photos from my iPhone?", "Most browsers cannot open HEIC. Export the photo to JPG from your phone or the Photos app first, then convert.")
]),

"image-to-base64": dict(
name="Image to Base64 Converter",
title="Image to Base64 Converter: Data URI Online | VipTools",
desc="Convert an image to a Base64 data URI for HTML, CSS or JSON. Copy the text in one click. Free, private and fast. Nothing is uploaded.",
extra=[
 ("What Base64 means for images", [
  "Base64 is a way of writing binary data as plain text using 64 safe characters. An image becomes a long string of letters, digits, plus and slash signs. Adding the prefix data:image/jpeg;base64, tells the browser how to read that text as a picture.",
  "Because the picture is now text, it can be stored inside HTML, CSS, JavaScript or JSON without a separate file."]),
 ("Using the output in HTML and CSS", [
  "In HTML, paste the full data URI as the src value of an img tag. In CSS, use it inside url() for a background image. Use the raw option only when a tool asks for the Base64 characters without the prefix, for example when filling a field in some APIs.",
  "Keep the data URI intact. A single missing character will stop the image from displaying."]),
 ("When Base64 helps", [
  "Very small images such as icons, spinners and logos can be embedded to save an extra request. Email templates often embed images because some email apps block external pictures. Developers also store tiny placeholder images inside configuration files or test data."]),
 ("When Base64 is a bad idea", [
  "Base64 increases the size of the data by roughly one third. A 300 KB photo becomes about 400 KB of text, which slows down page loading because the browser must read the whole string before showing the page. Embedded images also cannot be cached separately, so they download again every time the page loads.",
  "For photos and large graphics, keep the normal image file and link to it. Use Base64 only for small, frequently used graphics."]),
 ("Base64 is not security", [
  "Encoding is not encryption. Anyone who sees the string can decode it back into the original picture. Do not use Base64 to hide private images or secrets."])
],
faq=[
 ("Is my image uploaded to a server?", "No. The file is read by your browser and converted there. Nothing is sent over the internet."),
 ("Why is the output so long?", "Base64 turns every three bytes of the image into four text characters, which makes the output about one third larger than the file."),
 ("What is the data: prefix?", "It tells the browser the type of data and the encoding, for example data:image/png;base64, followed by the image text."),
 ("Which image formats work?", "JPG, PNG, GIF, WebP and SVG all work in browsers. Formats your browser cannot display, such as some HEIC files, will show an error."),
 ("Can I decode the text back to an image?", "Yes. Paste a data URI into the address bar or an img tag and the picture appears. Our Base64 Encoder and Decoder tool also handles plain text.")
]),

"image-rotator": dict(
name="Image Rotator",
title="Image Rotator: Rotate and Flip Photos Online | VipTools",
desc="Rotate an image 90 degrees left or right, flip it horizontally or vertically, then download it. Free, private, runs in your browser.",
extra=[
 ("Why photos come out sideways", [
  "Cameras record the image in the same way every time, and the phone then writes a rotation tag so software knows how to display it. Some apps and websites ignore that tag, so a portrait photo appears sideways. Scans, screenshots from some devices and images saved from certain apps can also end up rotated.",
  "Rotating the picture bakes the new orientation into the file, so it displays correctly everywhere, including in apps that ignore rotation tags."]),
 ("Flip versus rotate", [
  "Rotating turns the image around its centre. Flipping mirrors it: horizontal flip swaps left and right, and vertical flip swaps top and bottom. A mirrored image looks different from a rotated one, so check which change you need.",
  "Flip horizontal is often used for selfies taken with the front camera, because the camera shows a mirror image of your face and many people prefer the way they look in a normal mirror."]),
 ("Images with text", [
  "Rotating text upside down makes it hard to read in the preview. Use the rotate buttons in steps, and check the result before downloading. Flipping text reverses it, which is useful for designs but not for documents."]),
 ("Saving without losing quality", [
  "JPG is compressed each time it is saved, so repeated rotation and saving can add small artefacts. Rotate the picture in one step where you can, and keep the original file as a backup. PNG and other lossless formats do not lose detail when rotated, so use PNG for graphics that you edit several times."])
],
faq=[
 ("Does rotating reduce image quality?", "A single rotation of a JPG saves the picture again, which adds very slight compression loss. Rotating a PNG loses nothing."),
 ("Is my photo uploaded?", "No. Rotation and flipping run in your browser, and the original file stays on your device."),
 ("Why does the image size change?", "Rotating by 90 degrees swaps the width and height, so a landscape photo becomes portrait."),
 ("Can I rotate a transparent PNG?", "The download is saved as JPG for simplicity, so transparent areas turn white. For transparency, convert with the Image Format Converter after rotating."),
 ("Can I rotate by an exact angle like 45 degrees?", "This tool uses 90-degree steps, which covers most orientation fixes. Use an image editor for arbitrary angles.")
]),

}
