"""GROUP 4 — Write a complete program from the specification.

Work on paper first. You may use only Weeks 1-7 concepts. Do not use dictionaries,
functions that solve the entire task for you, list comprehensions, or while loops.

PARCEL-SORTING CENTRE

The centre has three delivery zones. A parcel belongs to a zone when its numeric
code is between that zone's start and end values, including both endpoints.

    zones  = ["North", "Central", "South"]
    starts = [1000, 2000, 3000]
    ends   = [1999, 2999, 3999]
    counts = [0, 0, 0]

PART A

Ask the user for parcel codes separated by commas, for example:

    1005,2050,3012,2500,1999

Separate and convert the codes. For every code, find its zone and increase the
matching position in counts. Print "Invalid code" for a code outside every range.

PART B

Print every zone and its parcel count. Then find and print the busiest zone without
using max(). If counts are tied, keeping the first busiest zone is acceptable.

Example output format:

    North: 2 parcels
    Central: 2 parcels
    South: 1 parcels
    Busiest zone: North

PART C

Ask for recipient names separated by semicolons. For each name, print "Priority"
if at least one of these statements is true:

- its lowercase form starts with "a";
- its lowercase form contains "silva";
- its lowercase form ends with "s".

Otherwise print "Normal". Include the original name in the message.

Example:

    Ana: Priority
    Bruno: Normal

Write your complete solution below this comment.
"""


zones = ["North", "Central", "South"]
starts = [1000, 2000, 3000]
ends = [1999, 2999, 3999]
counts = [0, 0, 0]

# TODO: Write Parts A, B, and C here.

