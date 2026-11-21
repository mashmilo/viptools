# Upgraded content for the remaining tools.
C = {
"timestamp-converter": {
 "extra": [
  ("What a Unix timestamp is", ["A Unix timestamp counts seconds since 1 January 1970 at 00:00:00 UTC. The value 0 is that moment itself, and 1000000000 is 9 September 2001 at 01:46:40 UTC. Because it is a single number with no time zone, it is easy to store, compare and sort."]),
  ("Common mistakes", ["Some systems store milliseconds rather than seconds. A value about 1000 times larger than expected usually means milliseconds, so divide by 1000 first. Also check the time zone: a timestamp is always UTC, while a displayed date may use local time. Compare both to avoid confusion across servers."]),
  ("Where timestamps are used", ["Databases, log files, APIs, JWT tokens and file systems all use Unix time. Developers convert timestamps when reading logs, debugging expiry times or comparing events from different services."]),
 ],
 "faq": [
  ("Is the timestamp in seconds or milliseconds?", "This converter treats the input as seconds. Divide a millisecond timestamp by 1000 before converting."),
  ("Which time zone does the output use?", "Compare the result with UTC and with your local time, since the display can differ depending on your device settings."),
  ("What is the Year 2038 problem?", "Systems that store Unix time in a signed 32-bit integer cannot represent dates after 19 January 2038. Modern systems use 64-bit values to avoid this."),
  ("Does the tool send my data anywhere?", "No. Conversions run in your browser."),
 ],
},
"text-to-binary": {
 "extra": [
  ("An example", ["The letter A is 65 in ASCII and 01000001 in 8-bit binary. The word Hi becomes two groups of eight bits, one for H and one for i. Spaces and punctuation have their own codes too."]),
  ("Why this matters", ["Binary is how computers store characters. Seeing the conversion helps students understand character encoding, and it is useful for classroom activities, puzzles and checking how a file or message is stored."]),
  ("Characters beyond basic English", ["Basic English letters use one byte each in UTF-8. Accented letters, symbols and emoji use more bytes, so their binary form is longer. This tool converts each character using its code, so check the result if you need an exact byte representation."]),
 ],
 "faq": [
  ("Does it support emoji and non-English letters?", "Characters outside basic ASCII use more than one byte in UTF-8, so the binary output is longer for them."),
  ("What is the difference between binary and ASCII?", "ASCII is a table that maps characters to numbers. Binary is how those numbers are written using only zeros and ones."),
  ("Can I convert binary back to text?", "Yes. Enter groups of eight bits separated by spaces to get the text back, if the tool offers the reverse conversion on the page."),
  ("Is my text uploaded?", "No. The conversion runs in your browser."),
 ],
},
"compound-interest-calculator": {
 "extra": [
  ("The formula", ["The amount after compounding is A equals P times (1 + r/n) to the power of nt. P is the starting amount, r is the annual rate as a decimal, n is the number of compounding periods per year, and t is the number of years. For example, 1,000 at 5% compounded monthly for 10 years grows to about 1,647."]),
  ("Why time matters", ["Growth accelerates because interest is earned on earlier interest. Starting early often matters more than the exact rate. Real investment returns vary and can be negative, unlike the steady rate used in this estimate."]),
  ("What the estimate leaves out", ["The calculator does not include taxes, fees, inflation or regular contributions. Inflation reduces the real value of money over time, and fees can reduce returns noticeably over decades. Consider these before relying on any projection."]),
 ],
 "faq": [
  ("Does this include taxes or fees?", "No. The calculator shows a simple estimate. Taxes, fees and inflation can reduce real returns."),
  ("Is a higher compounding frequency always better?", "It increases the result, but the effect is smaller than changes in the rate or the time."),
  ("Can I add regular monthly deposits?", "This version calculates growth on a single starting amount. Regular contributions need a separate calculation."),
  ("Is this financial advice?", "No. It is a general estimate. Speak to a qualified adviser before making investment decisions."),
 ],
},
"discount-calculator": {
 "extra": [
  ("An example", ["A 200 item with a 25% discount costs 150 and saves 50. The saving is 200 times 0.25, which is 50, and the sale price is 200 minus 50, which is 150."]),
  ("Stacked discounts", ["Two discounts applied one after another are not the same as adding their percentages. A 20% discount followed by 10% gives 200 times 0.8 times 0.9, which is 144. That is 28% off, not 30%. Retailers usually apply the first discount to the original price and the second to the reduced price."]),
  ("Working out the original price", ["If you know the sale price and the discount rate, divide the sale price by one minus the discount rate. A 150 item at 25% off was originally 150 divided by 0.75, which is 200. This is useful for checking whether a sale is genuine."]),
 ],
 "faq": [
  ("Does this include sales tax?", "No. Add tax after the discount if your local rules apply it to the sale price."),
  ("How do I work out the original price?", "Divide the sale price by one minus the discount rate. For example, 150 at 25% off was originally 150 divided by 0.75, which is 200."),
  ("Why are stacked discounts smaller than the sum?", "Each discount applies to the price left after the previous one, so the total reduction is less than adding the percentages."),
  ("Is the tool free?", "Yes, with no sign-up."),
 ],
},
"date-difference-calculator": {
 "extra": [
  ("An example", ["From 1 January to 1 March in a non-leap year is 59 days. Whether the end date is counted changes the total by one day, so check which convention your deadline, contract or project plan uses."]),
  ("Useful for", ["Calculating notice periods, contract terms, leave balances, project timelines and countdowns to events. Many contracts count days differently, so read the definition in the agreement before relying on the number."]),
  ("Working days are different", ["This calculator counts calendar days, including weekends and public holidays. If you need working days, subtract weekends and any holidays that apply in your location."]),
 ],
 "faq": [
  ("Does the end date count as a day?", "The calculator shows the simple difference between the two dates. Add one if you need both the start and end day included."),
  ("Does it account for leap years?", "Yes. The date system handles leap years automatically."),
  ("Can it count working days?", "This version counts calendar days. Exclude weekends and holidays manually if you need working days."),
  ("Are my dates stored?", "No. The calculation runs in your browser."),
 ],
},
"uuid-generator": {
 "extra": [
  ("What a UUID is", ["A UUID is a 128-bit identifier written as 32 hexadecimal digits in five groups, for example 123e4567-e89b-42d3-a456-426614174000. Version 4 UUIDs are generated from random numbers, so the chance of two being the same is extremely small."]),
  ("When to use one", ["Use UUIDs as database keys, request IDs, session references or file names when you need unique values without a central counter. They can be created on different machines without coordination."]),
  ("Good practice", ["Treat UUIDs as identifiers, not secrets. A UUID is not a password or access token. Use proper authentication for access control, and do not expose internal identifiers in public URLs if they should stay private."]),
 ],
 "faq": [
  ("Are the UUIDs truly random?", "The tool uses the browser's crypto.randomUUID function, which produces version 4 UUIDs from a cryptographic random source."),
  ("Can two UUIDs be the same?", "The chance is so small it is effectively zero for practical purposes."),
  ("Are generated UUIDs stored?", "No. They are created in your browser and not saved on our servers."),
  ("What is the difference between a UUID and a GUID?", "GUID is Microsoft's name for the same kind of 128-bit identifier. The formats are compatible."),
 ],
},
"image-compressor": {
 "extra": [
  ("How it works", ["The image is drawn onto a canvas in your browser and re-encoded as JPG at the quality you choose. Lower quality gives a smaller file with more visible artefacts. For many photos, values between about 60 and 80 balance size and quality well. Compare the original and compressed sizes shown on the page."]),
  ("Transparency and formats", ["JPG does not support transparency. Transparent areas of a PNG become white in the output. Keep the original PNG if you need a transparent background, and use a converter for other formats."]),
  ("Why smaller images help", ["Smaller images load faster, which improves the experience on slow connections and helps page speed scores. Google uses page experience as one of many signals, so compressing images is good practice rather than a guaranteed ranking boost."]),
 ],
 "faq": [
  ("Are my images uploaded?", "No. Compression happens in your browser, and the file never leaves your device."),
  ("Why is the output always JPG?", "JPG compresses photos much more than PNG. The tool outputs JPG, so PNG transparency is replaced with white."),
  ("Why did my image get bigger?", "Very small images or images that were already heavily compressed can grow slightly when re-encoded. Keep the original in that case."),
  ("Does compression help SEO?", "Smaller images load faster, which supports page speed. It is good practice but not a standalone ranking factor."),
 ],
},
"youtube-playlist-length-calculator": {
 "extra": [
  ("How the playlist lookup works", ["Paste a link to a public or unlisted YouTube playlist. The site reads the playlist's videos and their durations through the official YouTube Data API, adds them up, and shows the total at different playback speeds. Deleted and private videos are skipped and reported, since YouTube does not provide their durations."]),
  ("Playback speed", ["A playlist of 30 videos averaging 10 minutes is 300 minutes at normal speed, which is 5 hours. At 1.5x speed it is 200 minutes, or 3 hours and 20 minutes. Fast playback saves time, but very fast speeds can make complex content harder to follow."]),
  ("Planning with the total", ["Use the total to schedule a course, split a long tutorial series across weeks, or check whether a playlist fits into your day. Videos can be added or removed at any time, so check again before a long study session."]),
 ],
 "faq": [
  ("Can I use a private playlist?", "No. The playlist must be public or unlisted. Private playlists cannot be read."),
  ("Is the total exact?", "It is the sum of the video durations YouTube provides when the lookup runs. Playlists longer than the lookup limit are reported as partial."),
  ("Do I need to sign in to YouTube?", "No. You only paste the link. The site does not ask for your account."),
  ("Why is the total different from what I expected?", "Some videos may be deleted or private, and the playlist may have changed since the lookup. The page reports how many videos were skipped."),
  ("Can I estimate without a link?", "Yes. Enter the number of videos and their average length in minutes."),
 ],
},
}
