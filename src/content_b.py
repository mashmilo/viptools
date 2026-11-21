# Upgraded content for tools 10-18.
B = {
"percentage-calculator": {
 "extra": [
  ("Three common calculations", ["What is 15% of 200? Multiply 0.15 by 200 to get 30. What percent is 30 of 200? Divide 30 by 200 and multiply by 100 to get 15%. What is the change from 80 to 100? Subtract the old value from the new one, divide by the old value, and multiply by 100 to get a 25% increase."]),
  ("Why the base value matters", ["Percentages are always relative to a base. The most common mistake is taking a percentage of the wrong number. A 10% increase followed by a 10% decrease does not return you to the start: 100 rises to 110, then falls to 99. Percentages of different bases should not be added together."]),
  ("Where percentages show up", ["Discounts, sales tax, tips, exam scores, interest rates, budget shares and growth figures all use percentages. Checking the base value first, and writing down which number the percentage applies to, prevents most errors."]),
 ],
 "faq": [
  ("What is the difference between percent of and percent change?", "Percent of finds a share of a number. Percent change compares a new value with an old value."),
  ("Why is a percentage increase not reversed by the same percentage decrease?", "Percentages depend on the starting value. A 50% increase followed by a 50% decrease leaves you at 75% of the original number."),
  ("How do I calculate percentage points?", "Percentage points are the simple difference between two percentages. Going from 10% to 15% is a rise of 5 percentage points, which is a 50% relative increase."),
  ("Does the calculator round results?", "Results are shown with a few decimal places. Round further if your use case needs fewer digits."),
 ],
},
"bmi-calculator": {
 "extra": [
  ("How the formula works", ["BMI is your weight in kilograms divided by your height in metres squared. For example, 70 kg at 170 cm gives 70 divided by 1.70 squared, which is 24.2. Imperial users multiply weight in pounds by 703 and divide by height in inches squared, which gives the same result."]),
  ("What BMI does not measure", ["BMI does not separate fat from muscle, does not show where body fat is stored, and can be misleading for athletes, older adults, pregnant people and some ethnic groups. Health professionals often add waist measurement, blood pressure, blood tests and family history to assess health."]),
  ("When to talk to a doctor", ["If your BMI falls outside the normal range, or you have concerns about your weight, see a doctor or registered dietitian. They can consider your full health history, medications and goals. This calculator does not give medical advice, and its result is not a diagnosis."]),
 ],
 "faq": [
  ("What BMI categories are used for adults?", "The commonly used ranges are below 18.5 underweight, 18.5 to 24.9 normal, 25 to 29.9 overweight, and 30 or above obesity. Some regions and clinicians use different cut-offs."),
  ("Is BMI accurate for children?", "No. Children and teenagers are assessed with BMI-for-age percentiles, which this calculator does not provide."),
  ("Does my BMI tell me how healthy I am?", "Not on its own. BMI is a screening number. Other measures and a clinical check give a fuller picture."),
  ("Is my data saved?", "No. The calculation runs in your browser, and nothing is sent to our servers."),
 ],
},
"emi-calculator": {
 "extra": [
  ("The EMI formula", ["EMI equals P times r times (1 + r) to the power n, divided by ((1 + r) to the power n minus 1). P is the loan amount, r is the monthly interest rate (annual rate divided by 12 and by 100), and n is the number of monthly payments. For example, a loan of 500,000 at 9% for 5 years has an EMI of about 10,379 a month, with total interest of about 122,751."]),
  ("Comparing loan offers", ["Compare the total payment and total interest, not only the monthly instalment. A longer term lowers each payment but usually increases the total interest paid. Check fees, processing charges, insurance and prepayment rules, which this calculator does not include. Confirm the final figures with the lender before you commit."]),
  ("Reducing the cost of a loan", ["Paying a little extra each month reduces the principal faster and cuts total interest. Changing the amount or the term in this calculator shows how much a small change in the rate or term affects the total."]),
 ],
 "faq": [
  ("Is this a bank quote?", "No. It is an estimate from the amount, rate and term you enter. Lenders may add fees, insurance or different rounding."),
  ("Does a longer loan term always cost more?", "Usually. Stretching the term lowers each payment but adds interest over more months."),
  ("Does the calculator handle floating or reducing-balance interest?", "This calculator uses a standard fixed-rate amortising loan with equal monthly payments. Variable-rate loans will change over time."),
  ("Does the calculator store my numbers?", "No. The calculation runs in your browser."),
 ],
},
"random-number-generator": {
 "extra": [
  ("Common uses", ["Teachers draw random students to answer questions, game players roll virtual dice, and researchers choose random samples from a list. Set a minimum and a maximum, choose how many numbers you need, and generate them."]),
  ("Fair draws", ["Turn off duplicates when you need unique picks, such as choosing winners from a list of entrants. With duplicates off, each number in the range can appear only once in the result. Each possible number has the same chance of being chosen."]),
  ("Random is not the same as predictable", ["Random output cannot be predicted from previous results. The tool uses the browser's cryptographic random generator, which is designed for security-sensitive uses, so it is suitable for fair draws and for generating values that should not be guessed."]),
 ],
 "faq": [
  ("Are the numbers truly random?", "The tool uses the browser's crypto.getRandomValues function, which draws from the operating system's secure random source."),
  ("Can it generate decimals?", "This tool produces whole numbers within your range."),
  ("Are my settings saved?", "Some settings may be stored in your browser so they are there when you return. Nothing is sent to our servers."),
  ("Can I pick numbers without repeats?", "Yes. Turn duplicates off and the result will contain each number at most once."),
 ],
},
"color-converter": {
 "extra": [
  ("An example", ["The colour #6366F1 is rgb(99, 102, 241), which is roughly hsl(239, 84%, 67%). HEX is compact and common in CSS. RGB is useful when you need to adjust red, green or blue channels. HSL is useful when you want to make a colour lighter or darker while keeping its hue."]),
  ("Colour and readability", ["Converting a colour does not tell you whether text on it is readable. Check the contrast between text and background. The WCAG AA guideline asks for a contrast ratio of at least 4.5 to 1 for normal body text and 3 to 1 for large text."]),
  ("Working with colour in designs", ["Choose a base colour, convert it to HSL, then adjust lightness to create a palette of tints and shades. Keeping the hue the same creates a consistent look across buttons, backgrounds and highlights."]),
 ],
 "faq": [
  ("What is the difference between HEX and RGB?", "They describe the same colour. HEX writes the red, green and blue values in base 16, while RGB writes them in base 10."),
  ("Why use HSL?", "HSL separates hue from lightness and saturation, which makes it easier to create lighter or darker shades of one colour."),
  ("Does the tool check contrast?", "This tool converts colour formats. Use a contrast checker to test readability of text on a background."),
  ("Can I enter a three-digit HEX code?", "Short codes such as #09F are expanded to six digits, so #09F means #0099FF."),
 ],
},
"remove-duplicate-lines": {
 "extra": [
  ("An example", ["Pasting the lines apple, pear, apple and fig returns apple, pear and fig. The first occurrence of each line stays in its original position, so the order of your list is preserved."]),
  ("Typical uses", ["Clean a keyword list before uploading it to an advertising platform, merge two contact lists without sending duplicate messages, or tidy a copied log file before reading it. Removing repeats also makes it easier to count unique values."]),
  ("Check before you clean", ["Lines that look identical may differ in spaces or capital letters, and those differences affect the result. Trim extra spaces first if your data is inconsistent, and keep a copy of the original list in case you need to recover a line."]),
 ],
 "faq": [
  ("Does it sort the lines?", "No. It removes repeats and keeps the original order."),
  ("Is the comparison case-sensitive?", "Check the output carefully if capitalisation matters, since Apple and apple may be treated as different lines depending on the settings."),
  ("Does it upload my list?", "No. The cleaning happens in your browser."),
  ("Can I use it on very long lists?", "Very large lists may slow down older devices. Split very large files into smaller parts if needed."),
 ],
},
"slug-generator": {
 "extra": [
  ("An example", ["The title \"10 Best Tips for Better Sleep!\" becomes 10-best-tips-for-better-sleep. Lowercase letters, numbers and hyphens are safe and readable in web addresses, and they work reliably across servers and devices."]),
  ("SEO and slugs", ["Keep slugs short and descriptive, and include the main keyword once where it fits naturally. Avoid dates and IDs unless your content needs them, because evergreen pages are easier to keep up to date when the URL does not include a year. Changing a slug later needs a redirect from the old address so existing links keep working."]),
  ("Accents and special characters", ["Accented letters such as é become plain letters such as e, so URLs stay simple and easy to type. Symbols and punctuation are removed or turned into hyphens, which avoids encoding problems in links that are shared or pasted."]),
 ],
 "faq": [
  ("Why are slugs lowercase with hyphens?", "Lowercase letters with hyphens are readable and consistent. Mixed case and underscores can cause confusion or duplicate pages on some servers."),
  ("Do slugs affect rankings directly?", "Google has said that descriptive URLs help people and search engines understand a page, but the effect is small. Clear, useful content matters much more."),
  ("Should I include stop words such as a and the?", "Shorter slugs are easier to read. Remove stop words when it does not hurt clarity."),
  ("Can a slug be changed later?", "Yes, but set up a 301 redirect from the old URL to the new one so visitors and search engines are sent to the right place."),
 ],
},
"meta-tag-generator": {
 "extra": [
  ("What the tags do", ["The title tag is the clickable headline in search results. The meta description is the snippet below it. Neither directly sets your ranking, but a clear, accurate title and description make people more likely to click, and search engines may use them when deciding what to show."]),
  ("Length guidance", ["Search engines usually display about 50 to 60 characters of a title and about 150 to 160 characters of a description, although the exact limit depends on the characters used and the device. Write each one to describe the specific page, and avoid stuffing keywords or repeating the same text across pages."]),
  ("Where to place the tags", ["Put the tags inside the head section of the HTML page. Each page should have a unique title and description. Duplicate descriptions across many pages can make search results look repetitive."]),
 ],
 "faq": [
  ("Does Google always use my meta description?", "No. Google may write its own snippet from the page content when it expects that to match the search better."),
  ("Where do I paste the tags?", "Place them inside the head section of the HTML page, between the head tags."),
  ("Does the generator send my text anywhere?", "No. The HTML is built in your browser."),
  ("Should every page have an Open Graph tag?", "Open Graph tags control how a page looks when shared on social platforms. They are useful for pages you expect people to share."),
 ],
},
}
