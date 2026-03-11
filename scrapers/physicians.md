## NOTES
# (This data excludes information from 2020.)

The first time I served the data on Datasette, I didn't realize the data was this large. I imagined I had far less rows.
There is barely any rhyme or reason to how the number of doctors that get disciplined changes. At first, it seemed weird that the number of sanctions jumped by 12,000 between 2018 and 2019, increasing from 26,000 to nearly 39,000. But the figures dropped sharply between 2021 and 2020: almost a difference of 9,000.

The format doesn't render properly for most of the years.
The names appear under the header by the right of the actual name column, links appear under the names columnm etc.
Also, in the 2026 data, some names appear multiple times throughout the dataset. They have different row_ids, but they seem like the same entry pasted in.
A closer look suggests that the data for 2026 has been pasted repeatedly.
It is a little hard to tell if the same thing is happening for other years, because there is mostly no names. URL replaces the names.
The possiblity of repeated rows makes it unreliable, so I decided to end the server and edit the writer.writer_row line of the scraper.
But I stil cant get the names to appear, except in 2026, because the format is different.
