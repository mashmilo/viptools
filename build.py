import re, os, json, shutil, html, glob, sys, urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
SRC = REPO + '/src'
SRCTOOLS = SRC + '/tools-src'
OUT = REPO + '/dist'
sys.path.insert(0, SRC)
from content_more import MORE
from content_yt import Y
from content_img import I
from content_new import N
import datetime
TODAY = datetime.date.today().isoformat()
BASE = 'https://viptools.online'

shutil.rmtree(OUT, ignore_errors=True)
shutil.copytree(SRC, OUT, ignore=shutil.ignore_patterns('tools-src', 'content_*.py', '__pycache__', 'yt_override.txt'))

cfg = json.load(open(SRC + '/config.json'))
ADSENSE = cfg.get('adsenseClient', '').strip()
GAID = cfg.get('gaId', '').strip()
GSC = cfg.get('gscVerification', '').strip()
BING = cfg.get('bingVerification', '').strip()

LOGO = ('<svg width="32" height="32" viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="vtg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#6366f1"/><stop offset="1" stop-color="#06b6d4"/></linearGradient></defs>'
        '<rect width="64" height="64" rx="16" fill="url(#vtg)"/><path d="M16 20l16 28 16-28" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ICON_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'

CATS = [
    ('Text tools', 'Count, clean and transform text.',
     ['word-counter', 'case-converter', 'remove-duplicate-lines', 'slug-generator', 'text-to-binary', 'viral-hook-generator', 'text-to-speech']),
    ('Generators', 'Create passwords, IDs, numbers and placeholder content.',
     ['password-generator', 'uuid-generator', 'random-number-generator', 'lorem-ipsum-generator', 'meta-tag-generator']),
    ('Developer tools', 'Format, encode and decode the data developers handle every day.',
     ['json-formatter', 'base64-encoder-decoder', 'url-encoder-decoder', 'timestamp-converter', 'color-converter', 'github-uploader']),
    ('Calculators and converters', 'Health, age, date, percentage and time calculations.',
     ['bmi-calculator', 'age-calculator', 'date-difference-calculator', 'percentage-calculator', 'length-converter']),
    ('YouTube tools', 'Thumbnails, tags, channel IDs, timestamps and playlist length for creators and viewers.',
     ['youtube-thumbnail-downloader', 'youtube-tag-extractor', 'youtube-channel-id-finder', 'youtube-timestamp-link-generator', 'youtube-playlist-length-calculator']),
    ('Finance calculators', 'Estimate loans, savings growth and discounts.',
     ['emi-calculator', 'compound-interest-calculator', 'discount-calculator']),
    ('Media tools', 'Work with images in your browser.',
     ['image-compressor', 'image-resizer', 'image-format-converter', 'image-to-base64', 'image-rotator', 'image-background-remover', 'meme-generator', 'ai-video-clipper']),
]
CAT_OF = {s: c[0] for c in CATS for s in c[2]}

# ---------------------------------------------------------------- tool content
# extra: sections added below the original text. faq: (question, answer)
T = {}
def tool(slug, name, title, desc, extra, faq, unused=None):
    T[slug] = dict(name=name, title=title, desc=desc, extra=extra, faq=faq)

tool('word-counter', 'Word Counter', 'Word Counter: Count Words, Characters & Reading Time | VipTools',
 'Free word counter. Count words, characters, sentences, paragraphs and reading time as you type. Runs in your browser, nothing uploaded.',
 [('A worked example', ['Take the sentence "Free online tools are fast." It has 5 words and 28 characters including spaces, or 23 without spaces. Each run of characters between spaces counts as one word, so a number like 2,500 or an address like name@example.com also counts as one.']),
  ('Common uses', ['Students check essays against word limits. Freelancers invoice per word. SEO editors keep meta descriptions near 155 characters so search results do not cut them off.'])],
 [('Does the word counter save my text?', 'No. Counting happens in your browser and the tool does not send your text to a server.'),
  ('How is reading time calculated?', 'The estimate assumes an average adult reading speed of about 238 words per minute. Real reading speed varies with the material and the reader.'),
  ('Are hyphenated words counted as one?', 'Yes. Any run of characters separated by spaces counts as one word, which matches how most word processors count.'),
  ('Is there a length limit?', 'There is no fixed limit. Very large documents may feel slow on older phones.')])

tool('password-generator', 'Password Generator', 'Password Generator: Strong Random Passwords Online | VipTools',
 'Generate strong random passwords in your browser using secure randomness. Choose length and character types. Nothing is sent to a server.',
 [('What makes a strong password', ['Length matters more than cleverness. A 16-character password mixing upper and lower case letters, digits and symbols has far more possible combinations than a short word-based password, so guessing it is impractical. Use 16 characters or more wherever a site allows it.']),
  ('Keep passwords safe', ['Use a password manager so every account gets its own password. Never reuse a password across sites, and turn on two-factor authentication wherever it is offered.'])],
 [('Is the generated password sent anywhere?', 'No. The password is created in your browser with the browser\'s cryptographic random number generator (crypto.getRandomValues). It is not transmitted or stored by the tool.'),
  ('What length should I choose?', '16 characters or more is a good default for most accounts.'),
  ('Why would a site reject a password with symbols?', 'Some sites allow only certain symbols. Turn symbols off or generate a new password if a form rejects it.'),
  ('Should I reuse a generated password?', 'No. Generate a new password for each account and store it in a password manager.')])

tool('json-formatter', 'JSON Formatter', 'JSON Formatter & Validator: Format, Minify & Check JSON | VipTools',
 'Format, validate and minify JSON online. See clear error messages for invalid JSON. Free, fast and private, running in your browser.',
 [('Example', ['Pasting {"name":"VipTools","tools":25} gives an indented, readable structure with each key on its own line. Minifying the same data removes spaces and line breaks, which makes API payloads smaller.']),
  ('When to use it', ['Developers use a JSON formatter to read API responses, check config files before deploying, and find a missing comma or bracket. A clear error message points to the problem so you can fix it quickly.'])],
 [('Is my JSON uploaded?', 'No. Formatting and validation run in your browser.'),
  ('What is the difference between formatting and minifying?', 'Formatting adds indentation and line breaks for reading. Minifying removes all unnecessary whitespace for the smallest size.'),
  ('Why does my JSON show an error?', 'Common causes are trailing commas, single quotes instead of double quotes, unquoted keys and comments, which JSON does not allow.'),
  ('Does it validate against a schema?', 'The tool checks that the JSON syntax is valid. It does not check your data against a custom JSON Schema.')])

tool('case-converter', 'Case Converter', 'Case Converter: UPPERCASE, lowercase, Title Case Online | VipTools',
 'Convert text to UPPERCASE, lowercase, Title Case or Sentence case instantly. Paste your text and copy the result. Free and private.',
 [('Example', ['"the quick brown fox" becomes "The Quick Brown Fox" in Title Case and "The quick brown fox" in Sentence case. Use uppercase for short labels and headings only, since long uppercase text is harder to read.']),
  ('Tips for clean text', ['Convert text before you format it for a document or a website. Check headings in Title Case against your style guide, because rules for which small words stay lowercase differ between publishers.'])],
 [('Does the converter change my original text?', 'It shows the converted text in the output box. Your original input is not sent anywhere.'),
  ('What is Sentence case?', 'Sentence case capitalises only the first letter of each sentence, as in normal prose.'),
  ('Is Title Case the same in every style guide?', 'No. Guides such as AP and Chicago differ on which short words stay lowercase, so this tool capitalises each word in a simple way.')])

tool('lorem-ipsum-generator', 'Lorem Ipsum Generator', 'Lorem Ipsum Generator: Placeholder Text for Designs | VipTools',
 'Generate Lorem Ipsum placeholder text by paragraph, sentence or word count for mockups, layouts and web designs.',
 [('Why designers use placeholder text', ['Placeholder text lets you judge a layout before the real copy exists. Because it has a roughly normal distribution of letters and word lengths, it looks like real prose without distracting the reviewer with meaning.']),
  ('Choosing the right amount', ['Generate text close to the length of your final content. A product card needs a sentence or two, while a blog layout needs several paragraphs to show how line spacing and headings look.'])],
 [('Is the generated text random?', 'Yes. It uses Math.random, which is fine for placeholder text but is not suitable for anything security-related.'),
  ('Where does Lorem Ipsum come from?', 'It is adapted from a Latin text by Cicero and has been used as dummy text by printers and designers since the 1500s.'),
  ('Can I copy the output?', 'Yes. Select the text and copy it, then paste it into your design tool or code.')])

tool('base64-encoder-decoder', 'Base64 Encoder & Decoder', 'Base64 Encoder & Decoder Online: Encode and Decode Text | VipTools',
 'Encode text to Base64 or decode Base64 back to readable text. Free online Base64 tool that runs in your browser.',
 [('Example', ['The text "Hi" encodes to "SGk=" in Base64. Decoding "SGk=" returns "Hi". Base64 turns binary or text into a set of safe characters so it can travel through systems that only handle plain text.']),
  ('Important limits', ['Base64 is an encoding, not encryption. Anyone can decode it, so never use it to hide passwords or secrets. It also makes data about one-third larger than the original.'])],
 [('Is Base64 encryption?', 'No. Base64 is a reversible encoding and gives no security on its own.'),
  ('Why does Base64 output end with = signs?', 'The = signs are padding so the encoded length is a multiple of four characters.'),
  ('Does the tool send my data to a server?', 'No. Encoding and decoding happen in your browser.')])

tool('url-encoder-decoder', 'URL Encoder & Decoder', 'URL Encoder & Decoder: Encode and Decode URLs Online | VipTools',
 'Encode or decode URLs and query strings with percent-encoding. Turn spaces and special characters into safe URL text. Free and private.',
 [('Example', ['A space becomes %20 and an ampersand becomes %26. Encoding a search term such as "fish & chips" before adding it to a URL stops the ampersand from being read as a parameter separator.']),
  ('When you need it', ['Developers encode query parameter values, UTM tags and redirect targets. Decoding helps you read long tracking URLs and check what each parameter really contains.'])],
 [('Should I encode a whole URL or just a value?', 'Encode individual values, such as a query parameter, rather than the whole URL. Encoding the whole URL also converts the characters that separate its parts.'),
  ('What does percent-encoding mean?', 'Each unsafe character is replaced by a % sign followed by its hexadecimal byte value, for example %20 for a space.'),
  ('Does it store my URLs?', 'No. Encoding and decoding run in your browser.')])

tool('length-converter', 'Length Converter', 'Length Converter: Meters, Feet, Miles, Inches & More | VipTools',
 'Convert length units between meters, kilometers, miles, feet, inches, yards and centimeters. Instant, accurate results in your browser.',
 [('Example', ['One mile equals 1.609344 kilometers exactly. To convert feet to meters, multiply by 0.3048. A 6-foot person is therefore 1.8288 meters tall.']),
  ('Metric and imperial', ['Most of the world uses metric units, while the United States mainly uses imperial units for everyday measures such as height and road distance. Converters help when a product spec or travel guide uses the other system.'])],
 [('How accurate are the conversions?', 'The tool uses standard exact conversion factors, so results are as precise as the number of decimal places shown.'),
  ('Is the converter free?', 'Yes. There is no sign-up and no limit on conversions.')])

tool('age-calculator', 'Age Calculator', 'Age Calculator: Exact Age in Years, Months & Days | VipTools',
 'Calculate your exact age in years, months and days from your date of birth. Free, instant and private.',
 [('How it works', ['The calculator compares your date of birth with today\'s date and counts complete years, then the remaining months and days. Leap years are handled by the built-in date system.']),
  ('Useful for', ['Checking eligibility for age-based rules, filling in forms that ask for exact age, and seeing how many days old a baby or pet is.'])],
 [('Does it store my date of birth?', 'The tool runs in your browser. Your date is not sent to a server.'),
  ('Is the result the same as my official age?', 'It is a calculation from the dates you enter. Official records and age rules may use different cut-off dates.'),
  ('Can I calculate the age of someone else?', 'Yes. Enter any valid date of birth.')])

tool('percentage-calculator', 'Percentage Calculator', 'Percentage Calculator: Find Percent of a Number Online | VipTools',
 'Calculate a percentage of a number, what percent one number is of another, or the percentage change between two values.',
 [('Three common calculations', ['What is 15% of 200? That is 0.15 × 200 = 30. What percent is 30 of 200? That is 30 ÷ 200 × 100 = 15%. What is the change from 80 to 100? That is (100 − 80) ÷ 80 × 100 = 25% increase.']),
  ('Why it matters', ['Percentages appear in discounts, tax, test scores, budgets and growth figures. Checking the base value, the number you are taking the percentage of, is the most common source of mistakes.'])],
 [('What is the difference between percent of and percent change?', 'Percent of finds a share of a number. Percent change compares a new value with an old value.'),
  ('Why is my percentage change not the same going up and down?', 'Percentages depend on the starting value. A 50% increase followed by a 50% decrease does not return you to the original number.'),
  ('Does it round the results?', 'Results are shown with a few decimal places. Round further if your use case needs fewer.')])

tool('bmi-calculator', 'BMI Calculator', 'BMI Calculator: Body Mass Index from Weight & Height | VipTools',
 'Calculate your Body Mass Index (BMI) from weight in kilograms and height in centimeters. See the standard adult weight category instantly.',
 [('How the formula works', ['BMI is your weight in kilograms divided by your height in meters squared. For example, 70 kg at 170 cm gives 70 ÷ (1.70 × 1.70) = 24.2, which is in the normal range for adults.']),
  ('Limits of BMI', ['BMI does not separate fat from muscle, does not show where fat is stored, and can be misleading for athletes, older adults, pregnant people and some ethnic groups. Health professionals often use waist measurement and other checks alongside it.']),
  ('When to talk to a doctor', ['If your BMI puts you in an unusual range, or you have weight concerns, see a doctor or registered dietitian. They can take your full health history into account.'])],
 [('What BMI categories are used?', 'For adults, the commonly used ranges are: below 18.5 underweight, 18.5 to 24.9 normal, 25 to 29.9 overweight and 30 or above obesity.'),
  ('Is BMI accurate for children?', 'No. Children and teenagers are assessed with BMI-for-age percentiles, which this calculator does not provide.'),
  ('Is my data saved?', 'No. The calculation runs in your browser and nothing is sent to a server.')])

tool('emi-calculator', 'EMI Loan Calculator', 'EMI Calculator: Monthly Loan Payment, Interest & Total | VipTools',
 'Estimate your monthly loan EMI, total interest and total payment for home, car or personal loans. Adjust amount, rate and term.',
 [('The EMI formula', ['EMI = P × r × (1 + r)^n ÷ ((1 + r)^n − 1), where P is the loan amount, r is the monthly interest rate (annual rate ÷ 12 ÷ 100) and n is the number of monthly payments. For example, a 500,000 loan at 9% for 5 years gives an EMI of about 10,379 per month.']),
  ('Using the result', ['Compare total interest between offers, not just the monthly figure. A longer term lowers the EMI but usually raises the total interest paid. Check the bank\'s exact quote before you borrow, since fees and rounding rules can change the final figures.'])],
 [('Is this a bank quote?', 'No. It is an estimate from the amount, rate and term you enter. Lenders may add fees, insurance or different rounding.'),
  ('Does a longer loan term always cost more?', 'It usually does. Stretching the term lowers each payment but adds interest over more months.'),
  ('Does the calculator store my numbers?', 'No. The calculation runs in your browser.')])

tool('random-number-generator', 'Random Number Generator', 'Random Number Generator: Pick Numbers in Any Range | VipTools',
 'Generate random whole numbers within any range, with or without duplicates. Uses secure browser randomness. Free and instant.',
 [('How it is used', ['Teachers draw random students, game players roll virtual dice, and researchers pick random samples. Set a minimum and maximum, choose how many numbers you need, and generate.']),
  ('Fair draws', ['Turn off duplicates when you need unique picks, such as choosing winners from a list of entrants. Each number in the range has the same chance of being picked.'])],
 [('Are the numbers truly random?', 'The tool uses the browser\'s cryptographic random generator (crypto.getRandomValues), which is suitable for fair draws.'),
  ('Can it generate decimals?', 'This tool produces whole numbers within your range.'),
  ('Are my settings saved?', 'Some settings may be saved in your browser so they are there when you return. Nothing is sent to a server.')])

tool('color-converter', 'Color Converter', 'Color Converter: HEX, RGB & HSL Online | VipTools',
 'Convert colors between HEX, RGB and HSL codes. Paste one format and get the others instantly for CSS, design tools and code.',
 [('Example', ['The color #6366F1 is rgb(99, 102, 241) and roughly hsl(239, 84%, 67%). Use HEX for short CSS declarations, RGB when you need to adjust channels, and HSL when you want to change lightness or saturation while keeping the hue.']),
  ('Color in accessibility', ['Converting a color is not enough to check readability. Test text contrast against the background, aiming for at least 4.5:1 for normal body text under WCAG AA.'])],
 [('What is the difference between HEX and RGB?', 'They describe the same colour. HEX writes the red, green and blue values in base 16, while RGB writes them in base 10.'),
  ('Why use HSL?', 'HSL separates hue from lightness and saturation, which makes it easier to create lighter or darker shades of one colour.'),
  ('Does it check contrast?', 'This tool converts colour formats. Use a dedicated contrast checker to test readability.')])

tool('remove-duplicate-lines', 'Remove Duplicate Lines', 'Remove Duplicate Lines Online: Clean Lists Fast | VipTools',
 'Remove duplicate lines from any list, keeping the first occurrence. Clean email lists, keywords and logs in your browser.',
 [('Example', ['Pasting the lines "apple", "pear", "apple", "fig" returns "apple", "pear", "fig". The first occurrence stays in its original position, so the order of your list is preserved.']),
  ('Typical uses', ['Clean a keyword list before uploading it to an ad platform, merge contact lists, or tidy a copied log file before analysing it.'])],
 [('Does it sort the lines?', 'No. It removes repeats and keeps the original order.'),
  ('Is the comparison case-sensitive?', 'Check the output carefully if case matters, since "Apple" and "apple" may be treated as different lines depending on the setting.'),
  ('Does it upload my list?', 'No. The cleaning happens in your browser.')])

tool('slug-generator', 'Slug Generator', 'Slug Generator: Turn Titles into SEO-Friendly URLs | VipTools',
 'Turn any title into a clean, lowercase URL slug with hyphens. Remove accents and special characters for SEO-friendly web addresses.',
 [('Example', ['"10 Best Tips for Better Sleep!" becomes "10-best-tips-for-better-sleep". Lowercase letters, numbers and hyphens are safe and readable in web addresses.']),
  ('SEO tips for slugs', ['Keep slugs short and descriptive, and include the main keyword once. Avoid dates and IDs unless your content needs them. Changing a slug later requires a redirect from the old address.'])],
 [('Why are slugs lowercase with hyphens?', 'Lowercase letters with hyphens are readable and consistent. Underscores and mixed case can cause duplicate-content issues on some servers.'),
  ('Does the slug change accented letters?', 'The generator aims to convert accented letters to plain ASCII equivalents, so URLs stay simple.'),
  ('Does it affect ranking directly?', 'Google has said that a descriptive URL can help people and search engines understand a page, but the effect is small. Clear content matters much more.')])

tool('meta-tag-generator', 'Meta Tag Generator', 'Meta Tag Generator: Title & Description Tags for SEO | VipTools',
 'Create SEO meta title and meta description tags with length guidance, plus the matching HTML code to paste into your page head.',
 [('What the tags do', ['The title tag is the clickable headline in search results, and the meta description is the snippet beneath it. Neither directly sets your ranking, but a clear title and description encourage people to click.']),
  ('Length guidance', ['Titles are displayed up to about 60 characters before they may be truncated, and descriptions about 155 characters. Write each one to describe the specific page rather than the whole site.'])],
 [('Does Google always use my meta description?', 'No. Google may write its own snippet from the page content when it thinks that will better match the search.'),
  ('Where do I paste the tags?', 'Put them inside the head section of the HTML page, between the head tags.'),
  ('Does the generator send my text anywhere?', 'No. The HTML is built in your browser.')])

tool('youtube-playlist-length-calculator', 'YouTube Playlist Length Calculator', 'YouTube Playlist Length Calculator: Watch Time at Any Speed | VipTools',
 'Paste a YouTube playlist link to get its real total length, or estimate from video count. Watch time at 1x, 1.25x, 1.5x and 2x speed.',
 [('Example', ['A playlist of 30 videos averaging 10 minutes takes 300 minutes at normal speed, which is 5h 0m. At 1.5x speed the same playlist takes 200 minutes, or 3h 20m.']),
  ('Planning with the estimate', ['Use the result to schedule a course, split a long tutorial series across weeks, or decide whether a playlist fits into your day. Real videos vary in length, so build in some margin.'])],
 [('Is the total exact?', 'With a playlist link, the total is read from YouTube video durations. Deleted or private videos are skipped and reported. Playlists longer than 1000 videos are counted partially and the page says so. The manual estimate multiplies your video count by your average length.'),
  ('Do I need to sign in to YouTube?', 'No. The playlist must be public or unlisted. Private playlists cannot be read.'),
  ('Does playback speed change the total?', 'Yes. Watching at 2x speed halves the total time, although fast playback can make some content harder to follow.')])

tool('timestamp-converter', 'Unix Timestamp Converter', 'Unix Timestamp Converter: Epoch to Date & Back | VipTools',
 'Convert Unix epoch timestamps to human-readable dates and back. Shows the current timestamp in seconds. Free developer tool.',
 [('What a Unix timestamp is', ['A Unix timestamp counts seconds since 1 January 1970 at 00:00:00 UTC. For example, 0 is the epoch itself, and 1000000000 is 9 September 2001 at 01:46:40 UTC.']),
  ('Common pitfalls', ['Some systems store milliseconds rather than seconds, so a value 1000 times larger than expected usually means milliseconds. Always check the time zone, since a timestamp is UTC while the displayed date may use local time.'])],
 [('Is the timestamp in seconds or milliseconds?', 'This converter treats the input as seconds. Divide a millisecond timestamp by 1000 before converting.'),
  ('Which time zone does the output use?', 'Convert and check the result against UTC and your local time, since the display can differ depending on your device settings.'),
  ('Does the tool send my data anywhere?', 'No. Conversions run in your browser.')])

tool('text-to-binary', 'Text to Binary Converter', 'Text to Binary Converter: Encode Text as Binary Online | VipTools',
 'Convert text to binary code (ones and zeros) and back. See each character as its 8-bit binary value. Free and instant.',
 [('Example', ['The letter "A" is 65 in ASCII and 01000001 in 8-bit binary. A word like "Hi" becomes two 8-bit groups, one for H and one for i.']),
  ('Why learn this', ['Binary is how computers store text. Seeing the conversion helps students understand character encoding, and it is useful for puzzles and classroom activities.'])],
 [('Does it support emoji and non-English letters?', 'Characters outside basic ASCII use more than one byte in UTF-8, so the binary output is longer for them.'),
  ('What is the difference between binary and ASCII?', 'ASCII is a table that maps characters to numbers. Binary is how those numbers are written using only zeros and ones.'),
  ('Is my text uploaded?', 'No. The conversion runs in your browser.')])

tool('compound-interest-calculator', 'Compound Interest Calculator', 'Compound Interest Calculator: Savings & Investment Growth | VipTools',
 'See how savings grow with compound interest over time. Enter principal, rate, years and compounding frequency for an estimate.',
 [('The formula', ['A = P (1 + r/n)^(nt), where P is the starting amount, r the annual rate, n the number of compounding periods per year and t the years. For example, 1,000 at 5% compounded monthly for 10 years grows to about 1,647.'])
  ,('Why time matters', ['Growth accelerates over time because interest is earned on earlier interest. Starting early often matters more than the exact rate. Remember that real investment returns vary and can be negative, unlike the steady rate in this estimate.'])],
 [('Does this include taxes or fees?', 'No. The calculator shows a simple estimate. Taxes, fees and inflation can reduce real returns.'),
  ('Is a higher compounding frequency always better?', 'It increases the result, but the effect is small compared with the rate and time.'),
  ('Is this financial advice?', 'No. It is a general estimate. Speak to a qualified adviser before making investment decisions.')])

tool('discount-calculator', 'Discount Calculator', 'Discount Calculator: Sale Price & Savings Online | VipTools',
 'Calculate the sale price and the amount you save from a percentage discount. Quick, accurate and free.',
 [('Example', ['A 200 item with a 25% discount costs 150 and saves you 50. The discount is 200 × 0.25 = 50, and the sale price is 200 − 50 = 150.']),
  ('Stacked discounts', ['Two discounts applied one after another are not the same as adding their percentages. A 20% discount followed by 10% gives 200 × 0.8 × 0.9 = 144, which is 28% off, not 30%.'])],
 [('Does this include sales tax?', 'No. Add tax after the discount if your local rules apply it to the sale price.'),
  ('How do I work out the original price?', 'Divide the sale price by (1 minus the discount rate). For example, 150 at 25% off was 150 ÷ 0.75 = 200.'),
  ('Is the tool free?', 'Yes, with no sign-up.')])

tool('date-difference-calculator', 'Date Difference Calculator', 'Date Difference Calculator: Days Between Two Dates | VipTools',
 'Find the number of days between two dates. Useful for deadlines, countdowns, project planning and time tracking.',
 [('Example', ['From 1 January to 1 March in a non-leap year is 59 days. Whether you count the start or end day changes the total by one, so check which convention your deadline uses.']),
  ('Useful for', ['Calculating notice periods, contract terms, pregnancy or project timelines, and how long until an event.'])],
 [('Does the end date count as a day?', 'The calculator shows the simple difference between the two dates. Add one if you need both the start and end day included.'),
  ('Does it account for leap years?', 'Yes. The date system handles leap years automatically.'),
  ('Are my dates stored?', 'No. The calculation runs in your browser.')])

tool('uuid-generator', 'UUID Generator', 'UUID Generator: Random Version 4 UUIDs Online | VipTools',
 'Generate random version 4 UUIDs (GUIDs) for databases, APIs and apps. Create one or many, copy instantly. Free and private.',
 [('What a UUID is', ['A UUID is a 128-bit identifier written as 32 hexadecimal digits in five groups, for example 123e4567-e89b-42d3-a456-426614174000. Version 4 UUIDs are generated from random numbers, so collisions are extremely unlikely.']),
  ('When to use one', ['Use UUIDs as database primary keys, request IDs, or file names where you need unique values without a central counter.'])],
 [('Are the UUIDs truly random?', 'The tool uses the browser\'s crypto.randomUUID function, which produces version 4 UUIDs from a cryptographic random source.'),
  ('Can two UUIDs be the same?', 'The chance is so small it is effectively zero for practical purposes.'),
  ('Are generated UUIDs stored?', 'No. They are created in your browser and not saved on our servers.')])

tool('image-compressor', 'Image Compressor', 'Image Compressor: Reduce JPG & PNG Size Online | VipTools',
 'Compress and resize JPG and PNG images in your browser. Adjust quality, see the size saving and download. Images never leave your device.',
 [('How it works', ['The image is drawn onto a canvas in your browser and re-encoded as JPG at the quality you choose. Lower quality gives a smaller file with more visible artefacts. Values from about 60 to 80 often give a good balance for photos.']),
  ('Transparency note', ['JPG does not support transparency. Transparent areas of a PNG become white in the output. Keep the original PNG if you need a transparent background.'])],
 [('Are my images uploaded?', 'No. Compression happens in your browser, and the file never leaves your device.'),
  ('Why is the output always JPG?', 'JPG compresses photos much more than PNG. The tool outputs JPG, so PNG transparency is replaced with white.'),
  ('Does compression help SEO?', 'Smaller images load faster, which helps page speed. Google treats page experience as one of many signals, so compressing images is good practice rather than a guaranteed ranking boost.')])

for _slug, _d in Y.items():
    tool(_slug, _d['name'], _d['title'], _d['desc'], _d['extra'], _d['faq'])
for _slug, _d in I.items():
    tool(_slug, _d['name'], _d['title'], _d['desc'], _d['extra'], _d['faq'])
for _slug, _d in N.items():
    tool(_slug, _d['name'], _d['title'], _d['desc'], _d['extra'], _d['faq'])

# ----------------------------------------------------------------- templates
OV = cfg.get('toolOverrides', {})
for _s in T:
    if OV.get(_s, {}).get('name'): T[_s]['name'] = OV[_s]['name']
    if OV.get(_s, {}).get('desc'): T[_s]['desc'] = OV[_s]['desc']
    if _s in MORE:
        T[_s]['extra'] = MORE[_s]['extra']
        T[_s]['faq'] = MORE[_s]['faq']
ENABLED = [s_ for s_ in T if OV.get(s_, {}).get('enabled', True)]
_base = {s_: c_ for c_, _, ss_ in CATS for s_ in ss_}
def _cat(s_):
    return OV.get(s_, {}).get('category') or _base.get(s_, 'Calculators and converters')
CATS = [(n_, b_, [s_ for s_ in ENABLED if _cat(s_) == n_]) for n_, b_, _ in CATS]
CATS = [c_ for c_ in CATS if c_[2]]
CAT_OF = {s_: _cat(s_) for s_ in T}
def head_common(title, desc, canon, robots='index,follow', og_type='website', extra_head=''):
    gtag = ''
    if GAID:
        gtag = ('<script async src="https://www.googletagmanager.com/gtag/js?id=' + GAID + '"></script>'
                '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}'
                "gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500});"
                "gtag('js',new Date());gtag('config','" + GAID + "');</script>")
    adsense = ''
    if ADSENSE:
        adsense = ('<meta name="google-adsense-account" content="' + ADSENSE + '">'
                   '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + ADSENSE + '" crossorigin="anonymous"></script>')
    verif = ''
    if GSC: verif += '<meta name="google-site-verification" content="' + GSC + '">'
    if BING: verif += '<meta name="msvalidate.01" content="' + BING + '">'
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<title>' + html.escape(title) + '</title>'
        '<meta name="description" content="' + html.escape(desc, quote=True) + '">'
        '<meta name="robots" content="' + robots + ',max-image-preview:large">'
        '<link rel="canonical" href="' + canon + '">'
        '<meta name="application-name" content="VipTools">'
        '<meta property="og:site_name" content="VipTools">'
        '<meta property="og:type" content="' + og_type + '">'
        '<meta property="og:title" content="' + html.escape(title, quote=True) + '">'
        '<meta property="og:description" content="' + html.escape(desc, quote=True) + '">'
        '<meta property="og:url" content="' + canon + '">'
        '<meta name="twitter:card" content="summary">'
        '<meta name="theme-color" content="#6366f1">'
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">'
        '<script>try{var t=localStorage.getItem("vt-theme")||\"dark\";document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>'
        '<link rel="stylesheet" href="/style.css?v=10">'
        + verif + adsense + gtag + extra_head +
        '<script src="/site.js?v=10" defer></script></head>')

NAV_LINKS = [('/#tools', 'All tools'), ('/about.html', 'About'), ('/contact.html', 'Contact'), ('/privacy.html', 'Privacy'), ('/terms.html', 'Terms')]
SUN_SVG = '<svg class="i-sun" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON_SVG = '<svg class="i-moon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
BURGER_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'

def header():
    links = ''.join('<a href="%s">%s</a>' % (h, t) for h, t in NAV_LINKS)
    return ('<header class="site-header"><div class="w nav">'
        '<a class="brand" href="/">' + LOGO + '<div>Vip<span>Tools</span></div></a>'
        '<nav class="menu" aria-label="Main">' + links + '</nav>'
        '<div class="hbtns">'
        '<button class="icon-btn" id="tb" type="button" aria-label="Switch to light mode">' + SUN_SVG + MOON_SVG + '</button>'
        '<details class="mnav"><summary class="icon-btn" aria-label="Open menu">' + BURGER_SVG + '</summary>'
        '<nav class="mobile-menu" aria-label="Mobile">' + links + '</nav></details>'
        '</div></div></header>')

POPULAR = ['word-counter', 'password-generator', 'json-formatter', 'emi-calculator', 'image-compressor']

def footer():
    pop = ''.join('<a href="/tools/%s/">%s</a>' % (s_, T[s_]['name']) for s_ in POPULAR if s_ in T)
    pages = ''.join('<a href="%s">%s</a>' % (h, t) for h, t in [('/', 'Home'), ('/about.html', 'About'), ('/contact.html', 'Contact'), ('/privacy.html', 'Privacy Policy'), ('/terms.html', 'Terms')])
    return ('<footer class="site-footer"><div class="w foot">'
        '<div class="fbrand"><a class="brand" href="/">' + LOGO.replace('width="32" height="32"', 'width="26" height="26"') + '<div>Vip<span>Tools</span></div></a>'
        '<p>Free, fast and private online tools. Everything runs in your browser.</p></div>'
        '<div><nav class="flinks" aria-label="Site">' + pages + '</nav></div>'
        '<div><h3 class="fh">Popular tools</h3><nav class="flinks">' + pop + '<a href="/#tools">All tools</a></nav></div>'
        '</div><div class="w copy">&copy; 2026 VipTools.online</div></footer>')

def ldjson(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

ORG = {"@type": "Organization", "@id": BASE + "/#org", "name": "VipTools", "alternateName": ["Vip Tools", "VipTools.online"], "url": BASE + "/", "logo": BASE + "/favicon.svg"}

def page(title, desc, path, body, schema=(), robots='index,follow', og_type='website', extra_head='', status_note=''):
    canon = BASE + path
    sch = [ORG] + list(schema)
    return (head_common(title, desc, canon, robots, og_type, extra_head + ldjson({"@context": "https://schema.org", "@graph": sch}))
        + '<body>' + header() + '<main class="w">' + body + '</main>' + footer()
        + '<div class="cc" id="cc" hidden></div></body></html>')

def crumbs(items):
    # items: list of (label, url)
    parts = ['<a href="%s">%s</a>' % (u, l) for l, u in items[:-1]] + [items[-1][0]]
    return '<nav class="crumbs" aria-label="Breadcrumb">' + ' / '.join(parts) + '</nav>'

def crumb_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": l, "item": BASE + u} for i, (l, u) in enumerate(items)]}

# ------------------------------------------------------------- tool pages
def extract_tool(slug):
    s = open(SRCTOOLS + '/%s/index.html' % slug, encoding='utf-8').read()
    m = re.search(r'<div class="box" id="app">(.*?)</div><div class="ad"></div><article>', s, re.S)
    assert m, slug
    app = m.group(1)
    art = re.search(r'<article>(.*?)</article>', s, re.S).group(1)
    scr = re.search(r'</article>(.*?)</main>', s, re.S).group(1)
    sm = re.search(r'<script>(.*?)</script>', scr, re.S)
    assert sm, slug
    return app, sm.group(1), art

written = {}
for slug in ENABLED:
    t = T[slug]
    app, script, art = extract_tool(slug)
    if slug == 'youtube-playlist-length-calculator':
        ov = open(SRC + '/yt_override.txt', encoding='utf-8').read()
        app, script = ov.split('===SCRIPT===\n')
    if slug == 'bmi-calculator':
        app = app.replace('<h2 id="o"></h2>', '<p class="result" id="o" aria-live="polite"></p>')
    if slug == 'image-compressor':
        script = script.replace("c.getContext('2d').drawImage(im,0,0)",
            "(()=>{const x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,c.width,c.height);x.drawImage(im,0,0)})()")
    # keep the author's original intro/how/why, drop their thin FAQ paragraph (replaced below)
    art = art.split('<h2>Frequently asked questions</h2>')[0]
    art = art.replace('<p>', '<p>')  # no-op, keeps structure
    extra_html = ''.join('<h2>%s</h2>%s' % (h, ''.join('<p>%s</p>' % p for p in ps)) for h, ps in t['extra'])
    faq_html = '<h2>Frequently asked questions</h2>' + ''.join('<h3>%s</h3><p>%s</p>' % (q, a) for q, a in t['faq'])
    cat = CAT_OF[slug]
    same = [s for s in ENABLED if CAT_OF[s] == cat and s != slug]
    related = same[:4] if len(same) >= 4 else (same + [s for s in ENABLED if s != slug and s not in same])[:4]
    rel_html = ('<section class="related"><h2>Related tools</h2><div class="rel-grid">' +
        ''.join('<a class="card" href="/tools/%s/"><h3>%s</h3><p>%s</p></a>' % (s, T[s]['name'], T[s]['desc'].split('.')[0] + '.') for s in related) +
        '</div></section>')
    items = [("Home", "/"), ("Tools", "/#tools"), (t['name'], "/tools/%s/" % slug)]
    schema = [
        {"@type": "WebApplication", "@id": BASE + "/tools/%s/#app" % slug, "name": t['name'], "url": BASE + "/tools/%s/" % slug,
         "description": t['desc'], "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any",
         "browserRequirements": "Requires JavaScript", "isAccessibleForFree": True,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "publisher": {"@id": BASE + "/#org"}},
        crumb_ld(items),
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t['faq']]},
    ]
    body = (crumbs([(l, BASE + u if False else u) for l, u in items]) +
        '<h1>' + html.escape(t['name']) + '</h1><p class="lead">' + html.escape(t['desc']) + '</p>'
        '<div class="box" id="app">' + app + '</div>'
        '<div class="ad" aria-label="Advertisement"></div>'
        '<article>' + art + extra_html + faq_html + '</article>' + rel_html +
        '<div class="ad" aria-label="Advertisement"></div>'
        '<script>' + script + '</script>')
    page_html = page(t['title'], t['desc'], '/tools/%s/' % slug, body, schema=schema, og_type='article')
    os.makedirs(OUT + '/tools/%s' % slug, exist_ok=True)
    open(OUT + '/tools/%s/index.html' % slug, 'w', encoding='utf-8').write(page_html)
    written[slug] = t['name']

# ------------------------------------------------------------- home page
cards = ''
for name, blurb, slugs in CATS:
    cards += ('<section class="cat" id="%s"><h2>%s</h2><p class="muted">%s</p><div class="grid">' %
        (re.sub(r'\W+', '-', name.lower()).strip('-'), html.escape(name), html.escape(blurb)))
    for s in slugs:
        cards += ('<a class="card" data-q="%s" href="/tools/%s/"><h3>%s</h3><p>%s</p></a>' %
            (html.escape((T[s]['name'] + ' ' + T[s]['desc']).lower(), quote=True), s, html.escape(T[s]['name']), html.escape(T[s]['desc'].split('.')[0] + '.')))
    cards += '</div></section>'

home_body = ('<section class="hero"><h1>Free online tools that just work</h1>'
    '<p>VipTools (also written Vip Tools) is a collection of free tools for text, calculations, developers and images. Each tool runs in your browser, so the data you enter is processed on your device and is not uploaded to our servers.</p>'
    '<div class="search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>'
    '<input id="search" type="search" placeholder="Search tools (e.g. password, json, emi)" aria-label="Search tools"></div></section>'
    '<div class="ad" aria-label="Advertisement"></div>'
    '<div class="section-title" id="tools"><h2>All tools</h2><span id="toolCount">%d tools</span></div>'
    '<div id="catalog">%s</div><p class="muted" id="noMatch" hidden>No tools match your search.</p>'
    '<section class="intro"><h2>Why use VipTools?</h2>'
    '<p>Many everyday jobs take longer than they should: checking a word count for an essay, estimating a loan payment, formatting an API response or shrinking a photo before uploading it. VipTools puts simple, accurate versions of these tools in one place, with no sign-up and no software to install.</p>'
    '<p>Every calculator shows its formula or method, and the guides on each tool page explain what the results mean and where they have limits. Read our <a href="/about.html">About page</a> to learn how we build and check the tools, or <a href="/contact.html">contact us</a> with feedback.</p></section>'
    ) % (len(ENABLED), cards)
home_schema = [
    {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "VipTools", "alternateName": ["Vip Tools", "VipTools.online"], "publisher": {"@id": BASE + "/#org"}, "inLanguage": "en"},
    {"@type": "ItemList", "name": "VipTools free online tools", "numberOfItems": len(ENABLED),
     "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": T[s]['name'], "url": BASE + "/tools/%s/" % s}
                         for i, s in enumerate([x for c in CATS for x in c[2]])]},
]
open(OUT + '/index.html', 'w', encoding='utf-8').write(page(
    'VipTools: Free Online Tools for Text, Calculators, Developers & Images',
    'VipTools offers free, private online tools for text, calculators, developers, creators and images. No sign-up, and everything runs in your browser.',
    '/', home_body, schema=home_schema))

# ------------------------------------------------------------- static pages
def simple(title, desc, path, article):
    body = (crumbs([("Home", "/"), (title.split(' | ')[0], path)]) +
            '<article class="page">' + article + '</article>')
    return page(title, desc, path, body, schema=[crumb_ld([("Home", "/"), (title.split(' | ')[0], path)])])

ABOUT = '''<h1>About VipTools</h1>
<p>VipTools (also written Vip Tools) is a free collection of everyday online tools for text, calculations, developers and images. It was built to be fast, simple and private: most tools run entirely in your browser, and there is no sign-up.</p>
<h2>Who runs VipTools</h2>
<p>VipTools is operated by {OWNER}. The site is an independent project. You can reach the operator at <a href="mailto:contact@viptools.online">contact@viptools.online</a>.</p>
<h2>Our mission</h2>
<p>Many useful tasks, such as checking a word count, estimating a loan payment or formatting an API response, should take seconds. We build tools that load quickly, work on phones, tablets and desktops, and give clear results.</p>
<h2>How we build and check the tools</h2>
<p>Each tool is written to do one job. Calculators use standard formulas, and the tool page shows the formula or method in plain language. When we add or change a tool, we test typical inputs and edge cases such as zero, negative numbers and empty fields, and we review the explanatory text for accuracy. Where a result depends on assumptions, such as the average reading speed in the Word Counter, we say so on the page.</p>
<h2>Privacy first</h2>
<p>Tools process the text, numbers and images you enter on your own device. They are not uploaded to our servers. Some tools remember your last inputs in your browser's local storage so they are there when you return. Read our <a href="/privacy.html">Privacy Policy</a> for details about analytics and advertising.</p>
<h2>Accuracy and disclaimers</h2>
<p>Calculators such as EMI, BMI, compound interest and age calculators provide estimates for general information. They are not financial, medical or legal advice. Please consult a qualified professional before making important decisions.</p>
<h2>Corrections and feedback</h2>
<p>If you find an error or have a suggestion, please <a href="/contact.html">contact us</a>. We fix mistakes as soon as we can confirm them.</p>
<p class="muted">Last updated: November 20, 2026</p>'''

CONTACT = '''<h1>Contact us</h1>
<p>We welcome questions, feedback, bug reports and tool suggestions.</p>
<h2>Email</h2>
<p>Write to us at <a href="mailto:contact@viptools.online">contact@viptools.online</a>. We usually reply within 2 to 3 business days.</p>
<h2>What to include</h2>
<ul><li>The name of the tool or page you were using</li><li>What you expected to happen and what actually happened</li><li>Your browser and device, if you are reporting a bug</li></ul>
<h2>Business and advertising</h2>
<p>For partnership, advertising or licensing enquiries, email us with "Business" in the subject line.</p>'''

PRIVACY = '''<h1>Privacy Policy</h1>
<p class="muted">Last updated: November 20, 2026</p>
<p>VipTools.online ("we", "our", "us") respects your privacy. This policy explains what information we collect, how it is used and the choices you have.</p>
<h2>Text and files you process</h2>
<p>Our tools run in your browser. The text, numbers and images you enter are processed on your device and are not stored or sent to our servers by the tool itself. Some tools save your last inputs in your browser's local storage so they are there when you return. That data stays on your device, and you can clear it through your browser settings.</p>
<h2>YouTube lookup tools</h2>
<p>The YouTube Tag Extractor, Channel ID Finder and Playlist Length Calculator send the link, video ID, channel name or playlist ID you enter to our server. The server asks the YouTube Data API for the public details and returns them to you. We do not store these requests, and results may be cached for a short time to keep lookups fast. The Thumbnail Downloader loads images directly from YouTube, and the Download button sends the video ID to our server only to deliver the image file. Your use of YouTube is also subject to the <a href="https://www.youtube.com/t/terms" rel="noopener">YouTube Terms of Service</a> and <a href="https://policies.google.com/privacy" rel="noopener">Google Privacy Policy</a>.</p>
<h2>Analytics</h2>
<p>We use Google Analytics to understand how visitors use the site, such as which pages are popular and how people arrive. Analytics uses cookies and collects usage data such as pages viewed, approximate location and device type. Where consent is required, analytics cookies are set only after you accept them in our cookie banner.</p>
<h2>Search Console</h2>
<p>We use Google Search Console and Bing Webmaster Tools to monitor how our pages appear in search results. These services do not collect personal information from visitors.</p>
<h2>Advertising</h2>
<p>We use Google AdSense to display advertisements. Google and its partners, including DoubleClick, use cookies to serve ads based on your prior visits to this and other websites. Where personalised ads are not permitted or you have not consented, ads may be shown without personalisation.</p>
<p>You can opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" rel="noopener">google.com/settings/ads</a>, or by visiting <a href="https://www.aboutads.info/choices/" rel="noopener">aboutads.info/choices</a>. For more on how Google uses data, see <a href="https://policies.google.com/technologies/ads" rel="noopener">Google's ad technologies policy</a>.</p>
<h2>Cookies</h2>
<p>Cookies are small files stored on your device. We use cookies for analytics and advertising, which you can accept or reject in our cookie banner. We also store your theme preference (light or dark) and your cookie choice in your browser's local storage. You can disable cookies in your browser settings, though some features may not work as expected.</p>
<h2>Your rights</h2>
<p>Depending on where you live, you may have rights to access, correct or delete personal data we hold about you, to object to or restrict certain processing, and to withdraw consent. Residents of the European Economic Area, the United Kingdom and California may have additional rights under the GDPR, UK GDPR or CCPA/CPRA. To exercise any right, email <a href="mailto:contact@viptools.online">contact@viptools.online</a>. We do not sell personal information.</p>
<h2>Third-party links</h2>
<p>Our site may link to external websites. We are not responsible for their privacy practices.</p>
<h2>Children</h2>
<p>Our site is not directed at children under 13, and we do not knowingly collect personal information from them.</p>
<h2>Changes</h2>
<p>We may update this policy from time to time. Changes take effect when posted on this page, and the date at the top shows when it was last updated.</p>
<h2>Contact</h2>
<p>Questions about this policy? Email <a href="mailto:contact@viptools.online">contact@viptools.online</a>.</p>'''

TERMS = '''<h1>Terms of Use</h1>
<p class="muted">Last updated: November 20, 2026</p>
<p>By using VipTools.online you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Use of tools</h2>
<p>All tools are provided free of charge for personal and commercial use. You are responsible for checking results before relying on them, especially for financial, medical or legal decisions.</p>
<h2>No warranty</h2>
<p>The tools and content are provided "as is" without warranties of any kind. We do not guarantee that the site will be uninterrupted or error-free.</p>
<h2>Limitation of liability</h2>
<p>To the maximum extent permitted by law, VipTools is not liable for any loss arising from your use of the site or its tools.</p>
<h2>Acceptable use</h2>
<p>Do not use the site to break laws, attack or overload our services, scrape it at a rate that harms performance, or infringe others' rights.</p>
<h2>Intellectual property</h2>
<p>The site design, logo and written content belong to VipTools. You may not copy the site for commercial redistribution without permission. You may use the output of the tools freely.</p>
<h2>Third-party services</h2>
<p>The site displays advertising and uses analytics provided by third parties. Their use of data is described in our <a href="/privacy.html">Privacy Policy</a>.</p>
<h2>Changes and contact</h2>
<p>We may revise these terms at any time. Changes take effect when posted. Questions? Contact us at <a href="mailto:contact@viptools.online">contact@viptools.online</a>.</p>'''

ABOUT = ABOUT.replace('{OWNER}', cfg.get('ownerName') or 'the VipTools team')
open(OUT + '/about.html', 'w', encoding='utf-8').write(simple('About | VipTools', 'Learn about VipTools, a free collection of fast, private online tools and how we build and check them.', '/about.html', ABOUT))
open(OUT + '/contact.html', 'w', encoding='utf-8').write(simple('Contact | VipTools', 'Contact VipTools for questions, feedback, bug reports or tool suggestions.', '/contact.html', CONTACT))
open(OUT + '/privacy.html', 'w', encoding='utf-8').write(simple('Privacy Policy | VipTools', 'How VipTools handles your data, cookies, analytics and advertising, and your privacy choices.', '/privacy.html', PRIVACY))
open(OUT + '/terms.html', 'w', encoding='utf-8').write(simple('Terms of Use | VipTools', 'Terms of use for VipTools free online tools.', '/terms.html', TERMS))

open(OUT + '/404.html', 'w', encoding='utf-8').write(page('Page not found | VipTools',
    'The page you were looking for does not exist. Browse all free VipTools tools.', '/404.html',
    '<section class="page"><h1>Page not found</h1><p>The page you were looking for has moved or does not exist. Try one of our tools instead.</p><p><a class="btn" href="/">Browse all tools</a></p></section>',
    robots='noindex,follow'))

# ----------------------------------------------------------- site-wide files

all_urls = ['/', '/about.html', '/contact.html', '/privacy.html', '/terms.html'] + ['/tools/%s/' % s for c in CATS for s in c[2]]
sm = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in all_urls:
    sm.append('<url><loc>%s%s</loc><lastmod>%s</lastmod></url>' % (BASE, u, TODAY))
sm.append('</urlset>')
open(OUT + '/sitemap.xml', 'w', encoding='utf-8').write('\n'.join(sm) + '\n')

open(OUT + '/robots.txt', 'w').write('User-agent: *\nAllow: /\nDisallow: /admin/\nDisallow: /api/\n\nSitemap: https://viptools.online/sitemap.xml\n')
open(OUT + '/ads.txt', 'w').write(('google.com, pub-%s, DIRECT, f08c47fec0942fa0\n' % ADSENSE[len('ca-pub-'):]) if ADSENSE else '# AdSense line appears here after you set adsenseClient in the admin panel.\n')

headers = '''/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://pagead2.googlesyndication.com https://www.googleadservices.com https://tpc.googlesyndication.com https://*.doubleclick.net https://adservice.google.com https://*.adtrafficquality.google https://fundingchoicesmessages.google.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob: https:; font-src 'self' data:; connect-src 'self' https://api.github.com https://www.google-analytics.com https://*.google-analytics.com https://*.googletagmanager.com https://*.googlesyndication.com https://*.doubleclick.net https://*.adtrafficquality.google https://fundingchoicesmessages.google.com; frame-src https://googleads.g.doubleclick.net https://tpc.googlesyndication.com https://*.googlesyndication.com https://*.adtrafficquality.google https://www.google.com https://fundingchoicesmessages.google.com; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'self'

/style.css
  Cache-Control: no-cache

/site.js
  Cache-Control: no-cache

/config.json
  Cache-Control: no-cache

/admin/*
  X-Robots-Tag: noindex, nofollow
  Cache-Control: no-store
'''
open(OUT + '/_headers', 'w').write(headers)

cfg_out = dict(cfg)
cfg_out.pop('tools', None)
cfg_out['tools'] = [{'slug': s_, 'name': T[s_]['name'], 'desc': T[s_]['desc'], 'category': CAT_OF[s_], 'enabled': s_ in ENABLED} for s_ in T]
json.dump(cfg_out, open(OUT + '/config.json', 'w'), indent=1)

print('built pages:', len(ENABLED), 'tools; disabled:', [s_ for s_ in T if s_ not in ENABLED])

# ---- IndexNow (Bing and others): submit all URLs after each Cloudflare build ----
def indexnow_submit():
    key = (cfg.get('indexnowKey') or '').strip()
    if not re.fullmatch(r'[a-f0-9]{8,128}', key):
        return
    with open(OUT + '/%s.txt' % key, 'w') as f:
        f.write(key)
    if os.environ.get('CF_PAGES') != '1':
        print('IndexNow: key file written, submission skipped (not a Cloudflare build)')
        return
    urls = [BASE + u for u in all_urls]
    body = json.dumps({'host': 'viptools.online', 'key': key,
                       'keyLocation': BASE + '/%s.txt' % key, 'urlList': urls}).encode()
    req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body,
                                 headers={'Content-Type': 'application/json; charset=utf-8'}, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print('IndexNow: submitted', len(urls), 'URLs, status', r.status)
    except Exception as e:
        print('IndexNow: not accepted yet (the key file goes live with this deploy, so the next deploy should work):', e)

indexnow_submit()
