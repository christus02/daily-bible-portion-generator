# Generate the Daily Bible reading Portion
The Daily Bible reading portion can be generated using this code and sent out by any means

Every day a portion of 10 Bible verses are allocated and the last few verses and the end of the chapter are also intelligently allocated.

## Usage

The below functions calls can be used to generate a list of strings that contains a message with the daily portion.

Examples | Usage
------------ | -------------
Generate from a particular Book of Bible | `getBiblePortionFromBook("Romans")`
Generate from a particular Book of Bible from a specific chapter | `getBiblePortionFromBook("Romans", fromChapter=6)`
Generate from a particular Book of Bible only from a particular chapter | `getBiblePortionFromChapter(book="Romans", chapter=6)`