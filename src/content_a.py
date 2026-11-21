# Upgraded content for tools 1-9. Each entry adds sections and FAQs below the original article.
A = {
"word-counter": {
 "extra": [
  ("A worked example", ["Take the sentence \"Free online tools are fast.\" It has 5 words and 28 characters including spaces, or 23 without spaces. Each run of characters between spaces counts as one word. A number such as 2,500, or an address such as name@example.com, also counts as one word.", "Punctuation attached to a word does not create extra words. The word fast. is still one word, so the count matches what a reader would count by eye."]),
  ("Who uses a word counter", ["Students check essays against assignment limits, where going over or under can cost marks. Freelancers invoice clients per word and need an exact total before sending an invoice. Bloggers and SEO editors keep titles under about 60 characters and meta descriptions near 155, so search results are not cut off.", "Social media captions, product listings and form fields also have limits. The character count with and without spaces helps when the limit applies to letters only, such as a database column or a short code."]),
  ("Tips for better writing", ["Set a target length before you start, then use the counter while you edit rather than at the end. Long sentences of 30 words or more are harder to read, so the sentence count gives a quick check on rhythm. Paragraph counts show whether a page will look crowded on a phone."]),
 ],
 "faq": [
  ("Does the word counter save my text?", "No. Counting happens in your browser, and the text you paste is not sent to our servers by the tool."),
  ("How is reading time calculated?", "The estimate assumes an average adult reading speed of about 238 words per minute. Real reading speed depends on the material, the reader and whether they are skimming."),
  ("Are hyphenated words counted as one?", "Yes. Any run of characters separated by spaces counts as one word, which matches how most word processors count."),
  ("Why do my counts differ from another tool?", "Word counters differ on edge cases such as numbers, hyphens, and text with line breaks. For official limits, use the count from the system you are submitting to."),
  ("Is there a length limit?", "There is no fixed limit. Very large documents may feel slow on older phones."),
 ],
},
"password-generator": {
 "extra": [
  ("What makes a password strong", ["Length matters more than clever substitutions. A 16-character password that mixes upper and lower case letters, digits and symbols has far more possible combinations than a short word-based password, which makes guessing it by brute force impractical. Use 16 characters or more wherever a site allows it.", "Avoid passwords built from names, dates, dictionary words or keyboard patterns such as qwerty. Attackers try these first. Randomly generated passwords avoid those patterns entirely."]),
  ("Keeping passwords safe", ["Use a password manager so every account has its own password, and you only need to remember one master password. Never reuse a password across sites. If one site is breached, reused passwords let attackers try the same password on your email and banking accounts.", "Turn on two-factor authentication wherever it is offered, preferably with an authenticator app or a passkey rather than SMS codes."]),
 ],
 "faq": [
  ("Is the generated password sent anywhere?", "No. The password is created in your browser using the browser's cryptographic random number generator (crypto.getRandomValues). The tool does not transmit or store it."),
  ("What length should I choose?", "16 characters or more is a good default for most accounts. Use longer passwords for accounts that protect money, work systems or email."),
  ("A site rejected my password with symbols. What now?", "Some sites allow only certain symbols. Turn symbols off or generate a new password with a different setting if a form rejects it."),
  ("Should I reuse a generated password?", "No. Generate a new password for each account and store it in a password manager."),
  ("Can I check whether a password was leaked?", "This tool does not check breach databases. Some password managers and services offer breach checks that compare a hashed version of a password without revealing it."),
 ],
},
"json-formatter": {
 "extra": [
  ("A short example", ["Pasting {\"name\":\"VipTools\",\"tools\":25} gives an indented, readable structure with each key on its own line. Minifying the same data removes spaces and line breaks, which makes API payloads smaller and faster to send.", "JSON has strict rules: keys and strings need double quotes, trailing commas are not allowed, and comments are not part of the format. A formatter that reports the exact line and position of an error saves time when debugging."]),
  ("When developers use a JSON formatter", ["Developers paste API responses to read nested data, check configuration files before deploying, and compare payloads from two systems. Formatting makes the structure visible, so a missing bracket or a field in the wrong place is easier to spot.", "Minifying is useful before storing JSON in a database column, embedding it in HTML, or sending it over a slow connection. Keep a formatted copy for editing and a minified copy for production."]),
 ],
 "faq": [
  ("Is my JSON uploaded?", "No. Formatting and validation run in your browser, so private API responses stay on your device."),
  ("What is the difference between formatting and minifying?", "Formatting adds indentation and line breaks for reading. Minifying removes unnecessary whitespace for the smallest size. Both keep the same data."),
  ("Why does my JSON show an error?", "Common causes are trailing commas, single quotes instead of double quotes, unquoted keys, and comments, which JSON does not allow."),
  ("Does it check my data against a schema?", "The tool checks that the JSON syntax is valid. It does not validate your data against a custom JSON Schema."),
  ("Can it handle very large files?", "Very large files can slow down the browser. Split large inputs into smaller pieces when possible."),
 ],
},
"case-converter": {
 "extra": [
  ("Examples", ["\"the quick brown fox\" becomes \"THE QUICK BROWN FOX\" in uppercase, \"the quick brown fox\" in lowercase, \"The Quick Brown Fox\" in Title Case, and \"The quick brown fox\" in Sentence case. Each style suits a different purpose.", "Uppercase works for short labels, buttons and acronyms. Long uppercase text is harder to read, so use it sparingly in body copy."]),
  ("Title Case and style guides", ["Title Case is not standardised. Many style guides keep short words such as a, an, the, and, but and of in lowercase unless they begin the title. This tool capitalises each word in a simple way, so check headings against the style guide your publisher or brand uses."]),
  ("Clean text for the web", ["Consistent capitalisation makes headings easier to scan and looks more professional. Sentence case is often used for web headings and buttons, while Title Case is common in article titles. Apply the same rule across a site so readers are not distracted."]),
 ],
 "faq": [
  ("Does the converter change my original text?", "It shows the converted text in the output box. Your input is processed in your browser and not sent anywhere."),
  ("What is Sentence case?", "Sentence case capitalises only the first letter of each sentence, plus proper nouns if you correct them, as in normal prose."),
  ("Is Title Case the same in every style guide?", "No. Guides such as AP and Chicago differ on which short words stay lowercase. Check the rule your project follows."),
  ("Does it handle accented letters?", "Yes. Accented letters are converted along with the rest of the text, as supported by your browser."),
 ],
},
"lorem-ipsum-generator": {
 "extra": [
  ("Why designers use placeholder text", ["Placeholder text lets you judge a layout before the real copy exists. Its letter and word lengths look like ordinary prose, so the reviewer focuses on spacing, hierarchy and line length rather than on the meaning of the words.", "Using real words that mean nothing is also a reminder to replace the text before launch. Placeholder copy that goes live can damage trust and search performance."]),
  ("Choosing the right amount", ["Generate text close to the length of the final content. A product card needs a sentence or two, a news layout needs several paragraphs to show how headings, images and line spacing work together, and a long article template needs enough text to test scrolling and reading width."]),
 ],
 "faq": [
  ("Is the generated text random?", "Yes. It uses Math.random, which is fine for placeholder text but is not suitable for anything that needs security."),
  ("Where does Lorem Ipsum come from?", "It is adapted from sections of a Latin text by Cicero and has been used as dummy text by printers and designers since the 1500s."),
  ("Can I copy the output?", "Yes. Select the text and copy it, then paste it into your design tool or code."),
  ("Should I use placeholder text on a live site?", "No. Replace all placeholder copy with real content before publishing, since search engines and visitors both expect meaningful text."),
 ],
},
"base64-encoder-decoder": {
 "extra": [
  ("Examples", ["The text \"Hi\" encodes to \"SGk=\" in Base64, and decoding \"SGk=\" returns \"Hi\". Base64 represents binary data using 64 safe text characters, so it can travel through systems that only handle text, such as email bodies, JSON fields and URLs.", "Base64 output is about one third larger than the input, because every three bytes become four characters."]),
  ("Where Base64 is used", ["Developers use Base64 to embed small images in CSS or HTML, send attachments in email, pass binary values in API tokens and configuration files, and store binary data in text formats. Each use is a transport or storage convenience, not a protection for the data."]),
  ("Important limits", ["Base64 is an encoding, not encryption. Anyone can decode it, so never use it to hide passwords, keys or personal information. Use proper encryption or access control when data must stay private."]),
 ],
 "faq": [
  ("Is Base64 encryption?", "No. Base64 is a reversible encoding and gives no security on its own."),
  ("Why does Base64 output end with = signs?", "The = signs are padding, so the encoded length is a multiple of four characters."),
  ("Does the tool send my data to a server?", "No. Encoding and decoding run in your browser."),
  ("Can I decode any Base64 string?", "Only valid Base64 text decodes correctly. Check for missing padding, extra spaces or characters outside the Base64 set."),
 ],
},
"url-encoder-decoder": {
 "extra": [
  ("Examples", ["A space becomes %20 and an ampersand becomes %26. Encoding a search term such as \"fish & chips\" before adding it to a URL stops the ampersand from being read as a separator between parameters.", "Non-English letters are encoded as UTF-8 bytes. For example, the letter é becomes %C3%A9."]),
  ("When you need it", ["Developers encode query parameter values, UTM tracking tags, redirect targets and API arguments. Decoding helps you read long tracking URLs and check what each parameter really contains, which is useful when debugging analytics or marketing links."]),
  ("Encode values, not whole URLs", ["Encode each value separately rather than the full URL. Encoding a whole URL also converts the characters that structure it, such as the colon after https and the slashes, which breaks the link."]),
 ],
 "faq": [
  ("Should I encode a whole URL or just a value?", "Encode individual values, such as a query parameter, rather than the whole URL."),
  ("What does percent-encoding mean?", "Each unsafe character is replaced by a % sign followed by its hexadecimal byte value, for example %20 for a space."),
  ("What is the difference between encodeURI and encodeURIComponent?", "encodeURIComponent encodes everything that is not a letter, digit or a few safe marks, which makes it right for values. encodeURI leaves structural characters such as / ? & = alone, which makes it suitable only for whole URLs."),
  ("Does it store my URLs?", "No. Encoding and decoding run in your browser."),
 ],
},
"length-converter": {
 "extra": [
  ("Exact conversion factors", ["One mile equals exactly 1.609344 kilometres. One inch equals exactly 2.54 centimetres, and one foot equals 12 inches or 0.3048 metres. A 6-foot person is therefore 1.8288 metres tall.", "Because these factors are defined exactly, the results are precise to the number of decimal places shown. Rounding is the only source of small differences."]),
  ("Metric and imperial units", ["Most countries use metric units for everyday measurements. The United States mainly uses imperial units for height, road distance and building dimensions, while science and manufacturing often use metric. Converters help with product specifications, travel guides, sewing patterns and construction plans written in the other system."]),
 ],
 "faq": [
  ("How accurate are the conversions?", "The tool uses standard exact conversion factors, so results are as precise as the number of decimal places shown."),
  ("Is the converter free?", "Yes. There is no sign-up and no limit on conversions."),
  ("Does it convert area or volume?", "This tool converts lengths. Area and volume use the squares and cubes of the same factors, so convert the length first and then square or cube the result."),
  ("Why do I see a small difference from another converter?", "Some tools round intermediate values. This tool keeps full precision during the calculation and rounds only the displayed result."),
 ],
},
"age-calculator": {
 "extra": [
  ("How the calculation works", ["The calculator compares your date of birth with today's date, counts complete years, and then counts the remaining months and days. Leap years are handled by the built-in date system, so February 29 is counted correctly."]),
  ("Useful for", ["Checking eligibility for age-based rules, filling in forms that ask for exact age, and working out how many days old a baby, pet or project is. Parents often use it to see how many months old a child is for vaccination or development charts."]),
  ("Age in official records", ["Official age rules may count age on a specific date, such as the first day of a school year or a legal cut-off. The calculator shows age today, so compare it with the date that matters for your situation."]),
 ],
 "faq": [
  ("Does it store my date of birth?", "The tool runs in your browser, and your date is not sent to our servers."),
  ("Is the result the same as my official age?", "It is a calculation from the dates you enter. Official records and legal rules may use different cut-off dates."),
  ("Can I calculate someone else's age?", "Yes. Enter any valid date of birth."),
  ("Why does it show days as well as years?", "Showing years, months and days together gives a precise age, which is useful for babies, pets and project timelines."),
 ],
},
}
