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


## UPDATE
## A few sentences about the potential features of a news app using this data, and the caveats or things that would need to be addressed.

I think a news app using this data would be a searchable tool, so that users can easily look up doctors by name. A search bar instantly comes to mind when I think of presenting this kind of data as an app.
The app would work in such a way that when a user searches a doctor's name, it shows up if on the list. When they click on it, they are redirected to a page that has the details and a link to the pdf where the sanction details are recorded.

One caveat: doctors can have similar names, so it might help to be more accurate by allowing users search by doctors' license numbers.
While I think this might be helpful, I don't imagine license numbers to be something random people know about their doctors. Still I think it would be better to add that to the results, rather than just doctors' names.
If we had geographical data, that would have been another way to better reduce the possibility of mixing up doctors who might have the same names.