# Content for the YouTube tools. build.py registers each entry with tool(...).
# extra: sections added below the intro/how-to/why text. faq: (question, answer) pairs, also used for FAQ schema.
Y = {

"youtube-thumbnail-downloader": dict(
 name="YouTube Thumbnail Downloader",
 title="YouTube Thumbnail Downloader: Save HD Thumbnails | VipTools",
 desc="Paste a YouTube link to see and download its thumbnail in every available size, up to 1280x720 HD. Free, no sign-up, works on phones.",
 extra=[
  ("Thumbnail sizes explained", [
   "Every YouTube video has several thumbnail files. The maximum resolution version is 1280 x 720 pixels (16:9) and is the one most people want. The standard version is 640 x 480, high quality is 480 x 360, medium is 320 x 180 and the small default is 120 x 90.",
   "The maximum resolution file only exists when the uploader provided a large enough image. Older videos and some uploads do not have it, so the tool hides sizes that are not available for the video you entered. The 640 x 480, 480 x 360 and 120 x 90 versions are 4:3 and can contain black bars at the top and bottom, which is normal."]),
  ("Using thumbnails responsibly", [
   "A thumbnail belongs to the creator of the video. It is fine to save one as a reference, to study what makes a thumbnail work, or to use it in a review or discussion of that video where the law allows it. Do not upload someone else's thumbnail as your own and do not use it to imply that a video is yours.",
   "If you make your own thumbnails, YouTube recommends 1280 x 720 pixels at a 16:9 ratio. Looking at the thumbnails of top videos in your topic is a quick way to see which colours, faces and text sizes are common."]),
  ("Works with every kind of link", [
   "You can paste a normal watch link, a short youtu.be link, a Shorts link, a live link, an embed link or a mobile link. You can also paste only the 11-character video ID. The tool finds the ID and shows the thumbnails straight away."]),
 ],
 faq=[
  ("How do I download a YouTube thumbnail?", "Paste the video link into the box. The tool shows every available size. Press Download under the size you want and the JPG is saved to your device. On some phones the image may open in a new tab first, and you can then press and hold it to save."),
  ("Why is the maximum resolution size missing?", "YouTube only creates the 1280 x 720 file when the original upload image was large enough. If it is missing, use the next size down, which is 640 x 480."),
  ("What format are the downloaded thumbnails?", "They are JPG files, which is the format YouTube serves for video thumbnails."),
  ("Can I use a downloaded thumbnail on my own video?", "No. Thumbnails are the work of the video's creator. Use them for reference or where fair use or a licence allows, and make your own image for your own videos."),
  ("Does this work for private videos?", "No. A private video has no public thumbnail. The tool works for public and unlisted videos."),
  ("Does the tool store the links I enter?", "No. The link is read in your browser to find the video ID. When you press Download, the video ID is sent to our server only to fetch the image from YouTube as a file, and we do not keep it."),
 ]),

"youtube-tag-extractor": dict(
 name="YouTube Tag Extractor",
 title="YouTube Tag Extractor: See Any Video's Tags | VipTools",
 desc="Paste a YouTube video link to see its hidden tags and hashtags, count the characters and copy them in one click. Free, no sign-up.",
 extra=[
  ("Where YouTube tags are hidden", [
   "Tags are keywords that the uploader adds in YouTube Studio. YouTube does not show them on the watch page, so you cannot see them just by looking at a video. They are still part of the video's public data, and this tool reads them from there.",
   "Hashtags are different. They are the words starting with # in the title or description, and they are visible on the page. The tool lists those too, so you get both sets in one place."]),
  ("How much do tags matter?", [
   "YouTube's own guidance says tags play a minor role in how videos are found. They are most useful when your topic is often misspelled, for example a product or a person with a hard spelling. Your title, thumbnail and description matter far more than tags.",
   "Because of that, use extracted tags as ideas, not as a recipe. Look at which phrases competing videos use, then keep the ones that honestly describe your own video."]),
  ("The 500 character limit", [
   "YouTube allows up to 500 characters in total for the tags field. Commas between tags are included in some counts, and a tag with spaces counts as one tag but may be wrapped in quotation marks. The tool shows the total length of the extracted tags so you can see how close a video is to the limit."]),
 ],
 faq=[
  ("Can I see the tags of any YouTube video?", "You can see the tags of any public or unlisted video where the creator added tags. If the creator added none, the tool tells you so."),
  ("Why does a video show no tags?", "Many creators leave the tags field empty because YouTube says tags have only a small effect. A video with no tags still has a title, description and hashtags that help people find it."),
  ("Are tags and hashtags the same?", "No. Tags are hidden keywords added in YouTube Studio. Hashtags are visible words that begin with # in the title or description. The tool shows both."),
  ("Should I copy a competitor's tags exactly?", "It is better to use them as ideas. Pick the phrases that describe your own video and leave out the rest, because tags that do not match your content do not help and can look like spam."),
  ("Does the tool send my link to a server?", "Yes. The video ID is sent to our server, which asks the YouTube Data API for the video's public details. We do not store the link, and the result is cached for a short time so that repeated lookups are fast."),
  ("Is there a limit on lookups?", "The tool relies on a daily YouTube quota shared by all visitors. If the quota is used up, the page asks you to try again later."),
 ]),

"youtube-channel-id-finder": dict(
 name="YouTube Channel ID Finder",
 title="YouTube Channel ID Finder: Get the ID from a URL or @Handle | VipTools",
 desc="Find any YouTube channel ID from a channel link, @handle or video link. Copy the UC ID, channel name and public stats instantly. Free.",
 extra=[
  ("What a channel ID is", [
   "A channel ID is the permanent identifier that YouTube gives to a channel. It is 24 characters long and starts with UC, for example UCxxxxxxxxxxxxxxxxxxxxxx. Unlike a name or an @handle, the ID never changes, even when the creator renames the channel.",
   "Many links and tools need this ID rather than the handle. Since handles were introduced in 2022, the channel page address often shows only the @handle, so the ID is not visible at a glance."]),
  ("Where you need a channel ID", [
   "Common uses include building a channel RSS feed, which follows the pattern https://www.youtube.com/feeds/videos.xml?channel_id= followed by the ID, connecting a channel to a third-party analytics or automation tool, using the YouTube Data API, and adding a channel to embeds or plugins that ask for it."]),
  ("Accepted input", [
   "You can paste a channel link with an @handle, a link that already contains the channel ID, an older /user/ or /c/ link, a link to any video or Short from the channel, or just the handle or the ID. If the input is only a custom name, the tool looks for the closest matching channel and marks the result so that you can check it."]),
 ],
 faq=[
  ("How do I find a YouTube channel ID?", "Paste the channel link, the @handle or a link to any of its videos into the box and press Find channel ID. The ID starting with UC appears with a Copy button."),
  ("Is the channel ID the same as the @handle?", "No. The handle is a readable name that the creator can change. The ID is permanent and always starts with UC."),
  ("Can I find the channel ID from a video link?", "Yes. Paste any public video or Shorts link and the tool returns the ID of the channel that uploaded it."),
  ("Why does the tool say the result is the closest match?", "When the input is only a custom name and not a handle or an ID, the tool has to search for it. Check the channel name and picture before you rely on the ID."),
  ("Does it work for any channel?", "It works for public channels. Terminated or private channels cannot be looked up."),
  ("Does the tool store what I search for?", "No. The text you enter is sent to our server only to ask the YouTube Data API for the channel, and we do not keep it. Results are cached briefly to keep lookups fast."),
 ]),

"youtube-timestamp-link-generator": dict(
 name="YouTube Timestamp Link Generator",
 title="YouTube Timestamp Link Generator: Start at Any Time | VipTools",
 desc="Create a YouTube link that starts at an exact time. Enter minutes and seconds, copy the short link, full link or embed URL. Free and instant.",
 extra=[
  ("How timestamp links work", [
   "A timestamp link is a normal YouTube link with a time added. The time is written in seconds after t=, so a link that starts at 1 minute 30 seconds ends with t=90. A short link looks like https://youtu.be/VIDEOID?t=90 and a full link looks like https://www.youtube.com/watch?v=VIDEOID&t=90s.",
   "For embedded players the parameter is called start, for example https://www.youtube.com/embed/VIDEOID?start=90. The tool gives you all three versions."]),
  ("When timestamp links help", [
   "Share the exact moment of a long video with a friend, point students to the right part of a lecture, link to a recipe step, or add a link in a blog post or a comment so readers land on the part that matters. It saves the viewer from scrubbing through the video."]),
  ("Time formats the tool understands", [
   "You can type the time in the hours, minutes and seconds boxes, or paste a link that already has a time. Existing values such as t=90, t=1m30s, t=1h2m3s and start=90 are read and shown in the boxes so you can adjust them."]),
 ],
 faq=[
  ("How do I link to a specific time in a YouTube video?", "Add ?t= and the number of seconds to a youtu.be link, or &t= to a watch link. The tool does the arithmetic for you from hours, minutes and seconds."),
  ("How do I convert minutes and seconds to a timestamp?", "Multiply the minutes by 60 and add the seconds. For example 2 minutes 15 seconds is 135 seconds, so the link ends with t=135."),
  ("What is the difference between t and start?", "The t parameter is used in normal links. The start parameter is used in embed URLs for the video player on a web page."),
  ("Will the link work on mobile and in the app?", "Yes. Links that use the t parameter open at that time in the YouTube app and in mobile browsers."),
  ("What happens if the time is longer than the video?", "The player ignores a time that is past the end of the video or starts it from the beginning, so check the length of the video before sharing."),
  ("Does the tool upload my link?", "No. The link and the time are processed in your browser and nothing is sent to a server."),
 ]),
}
