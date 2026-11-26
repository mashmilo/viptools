# Content for the new media and text tools. build.py registers each entry with tool(...).
# extra: sections added below the intro/how-to/why text. faq: (question, answer) pairs, also used for FAQ schema.
N = {

"image-background-remover": dict(
name="Image Background Remover",
title="Image Background Remover: Remove Photo Backgrounds Free Online | VipTools",
desc="Remove a photo background in your browser, touch up edges with a brush, then download a transparent PNG or add a new colour or image. Free and private.",
extra=[
 ("How the background is detected", [
  "The tool reads the colours along the edges of your picture and assumes the most common one is the background. It then removes every connected area close to that colour, so a plain white or grey wall disappears while similar colours inside the subject are kept.",
  "Use the Pick background colour button to click the background yourself if the detected colour is wrong, for example on a green screen or a coloured studio sheet."]),
 ("Getting a clean edge", [
  "Move the tolerance slider to decide how close a colour must be to count as background. A low value keeps more of the subject, and a high value removes more of the background. Shadows and soft edges often need a little brush work.",
  "Use the Erase brush to remove leftover background, and the Restore brush to bring back parts that were cut out by mistake. Reset touch-ups starts again from the automatic result."]),
 ("Choosing a new background", [
  "Transparent is best for logos, product photos and designs that will sit on other colours. A solid colour suits listings and ID photos, and an image background lets you place the subject on a scene. The download is always a PNG so the transparency is kept.",
  "Large photos are scaled down to 2048 pixels on the longest side for smooth editing, so the download has that maximum size."]),
],
faq=[
 ("Is my photo uploaded anywhere?", "No. The image is processed in your browser and the tool does not send it to a server."),
 ("Does this use artificial intelligence?", "No. It uses colour detection and a brush you control. It works best on plain or evenly coloured backgrounds. Busy scenes need more brush work."),
 ("Why does part of my subject disappear?", "The subject may contain a colour close to the background. Lower the tolerance slider or use the Restore brush over the missing part."),
 ("Can I keep the background in the original image?", "Yes. Set the background option to Image and choose a picture, or pick a solid colour. Transparent is only one of the options."),
 ("What file type do I get?", "A PNG file. PNG supports transparency, so the cutout keeps clean edges on any background."),
]),

"meme-generator": dict(
name="Meme Generator",
title="Meme Generator: Add Top and Bottom Text to Images Free | VipTools",
desc="Make a meme from your own picture. Add top and bottom captions in bold classic style, adjust the text size and download a PNG. Free, private and no sign-up.",
extra=[
 ("The classic meme layout", [
  "The traditional meme puts short bold text at the top and a punchline at the bottom, both in white with a black outline so they stay readable on bright and dark pictures. The generator follows this layout and wraps long captions onto extra lines automatically.",
  "Keep each caption short. Most readers take in a meme in a second or two, so a few punchy words usually work better than a full sentence."]),
 ("Choosing a picture", [
  "Pick a photo with a clear subject and a simple background, so the text does not compete with busy details. Close-up faces, animals and reaction shots are popular because the expression does much of the work.",
  "Large photos are scaled down for the preview, and the download keeps the size of the scaled picture, up to 1200 pixels wide."]),
],
faq=[
 ("Is my image uploaded?", "No. The picture is drawn on a canvas inside your browser and is never sent to a server."),
 ("Can I use any picture?", "You can use any image you have the right to share. Avoid copyrighted images, such as film stills or photos taken by others, unless you have permission."),
 ("What font is used?", "The tool uses Impact, a common bold meme font, when it is installed on your device. Otherwise it uses Arial Black or Arial."),
 ("Why is my text cut off?", "The text is wrapped to the picture width. Reduce the text size slider or shorten the caption if it still goes beyond the edge."),
]),

"text-to-speech": dict(
name="Text to Speech",
title="Text to Speech: Read Text Aloud Online Free | VipTools",
desc="Turn any text into speech in your browser. Choose a voice, set the speed and pitch, and listen instantly. Free, no sign-up, and your text is not stored.",
extra=[
 ("Voices depend on your device", [
  "Text to speech uses the voices installed in your browser or operating system, so the list differs between Windows, macOS, Android, iOS and Chrome. Some browsers add more voices after a moment, which is why the list may update on its own.",
  "A natural-sounding voice makes long text easier to follow. Try a few options on a short sample before you listen to a long article."]),
 ("Making the speech easier to follow", [
  "Slow the speed to about 0.9x for technical or unfamiliar material. Use paragraphs and punctuation in your text, since full stops and commas make the voice pause at natural points.",
  "Very long text can stop early in some browsers. If that happens, split the text into sections and press Speak on each one."]),
],
faq=[
 ("Can I download the audio as an MP3?", "Not with this tool. Browsers do not offer a way to save speech as a file, so the tool plays the audio live."),
 ("Is my text stored or sent anywhere?", "No. The text is read by your browser's built-in speech system and the tool does not store it."),
 ("Why are some voices missing?", "The available voices come from your device and browser. You can install more voices in your operating system's accessibility or speech settings."),
 ("Does it work on phones?", "Yes, in most modern mobile browsers. Volume and silent mode on the phone can affect what you hear."),
]),

"viral-hook-generator": dict(
name="Viral Hook Generator",
title="Viral Hook Generator: Free Hooks for YouTube, TikTok & Reels | VipTools",
desc="Generate eight scroll-stopping hooks for your YouTube video, TikTok, Reel, Short or blog post. Enter your topic, pick a platform and copy the list. Free.",
extra=[
 ("What makes a hook work", [
  "A good hook does one of three things quickly: it names a problem the viewer has, promises a clear result, or raises a question the viewer wants answered. Specific details such as a number, a timeframe or a surprising comparison make a hook more believable.",
  "Hooks are usually the first one or two seconds of a video or the first sentence of an article. Write the rest of the content to deliver on whatever the hook promised."]),
 ("Using a generated hook", [
  "Treat each line as a starting point. Replace the generic words with your own examples, and keep the promise honest. Clickbait that the content does not deliver tends to lower watch time and trust.",
  "Test two or three hooks on the same topic. Short video platforms and search results reward the versions that keep people watching or reading."]),
],
faq=[
 ("Does this tool use AI?", "No. The hooks come from proven patterns filled in with your topic. They are generated in your browser and nothing is sent to a server."),
 ("Can I use these hooks in my content?", "Yes. Edit them to fit your voice and your topic. The tool does not claim any rights to the text you create with it."),
 ("Will these hooks guarantee more views?", "No hook can guarantee results. A good hook helps people start watching or reading, and the rest of your content decides whether they stay."),
 ("Why do two hooks sometimes look similar?", "Each hook comes from a pattern, so different topics can produce similar wording. Edit the lines to give each one a clear angle."),
]),

"github-uploader": dict(
name="GitHub Uploader",
title="GitHub Uploader: Upload Files to a Repo in One Commit | VipTools",
desc="Upload files straight to a GitHub repository from your browser in one commit. Works with any file type. Free, no install, token never stored.",
extra=[
 ("Before you start", [
  "Create a fine-grained personal access token on GitHub and limit it to the one repository you want to use. Give it Contents permission set to read and write. A narrow token means a leaked token can only affect that repository.",
  "The repository needs at least one commit before uploads work, because the tool adds files to an existing branch."]),
 ("What happens when you upload", [
  "Each file is stored as a blob, then the tool builds a new tree and one commit on top of your branch. Existing files in other folders are left as they are. A file with the same path is replaced in the new commit, so use a different folder or name if you want to keep both versions.",
  "Files up to 25 MB each are supported. Very large files are better added with Git itself or GitHub Releases."]),
],
faq=[
 ("Is my token stored or sent to VipTools?", "No. The token stays in the page while you use it and is sent only to api.github.com, which is GitHub's own API. It is not saved in your browser or on our server."),
 ("Why does it ask for Contents permission?", "Contents permission lets the token read and write files in the repository. Without it GitHub will refuse the upload."),
 ("Why are all files in one commit?", "A single commit keeps your history clear and is faster than one commit per file."),
 ("Can I upload to a branch other than main?", "Yes. Type the branch name in the Branch field. The branch must already exist."),
],
),

}
