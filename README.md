# BIP-39 Seed Phrase Generator
- Generate seed phrases of lengths 12, 15, 18, 21, or 24 words.
- Option to display verbose output, including the binary representation of the seed phrase.
## Getting started 🚀 
Usage:
```bash
python3 seed_phrase_generator.py --seed_phrase_length=<length> --verbose=<True/False>

python3 seed_phrase_generator.py -h
```

##### ⚠️ Warning
Write down the seed phrase on paper and DO NOT copy it to the clipboard. This is a SECRET. Close the session when done.
Keep it in a safe place. Do not share it with anyone. Do not take pictures of it. This seed phrase is the key to your wallet.


### Dependencies  ⚠️
`pip install fire termcolor`

- To be demonstrative, use `.gif` instead of many screenshots. I use [CleanShot](https://cleanshot.com/) for this.
![gif example](https://public-bk-for-pics.s3.ca-central-1.amazonaws.com/git-template/CleanShot+2022-06-09+at+18.29.59.gif)


### About BIP39
- In the seed phrase the last word is not random. The portion of last word is a checksum.

1. Generate a random 128 bits (this is **entropy**)
2. Calculate the sha256 checksum of the **entropy**
3. Slice begingging of the checksum and append it to the **entropy**. Slice size is `Number_of_words/3` or `Seed_lenght/33`. (Example: 12 words seed phrase is 4 bits for the checksum)
4. Split result by segments of 11 bits. (Each word in BIP39 list (2048 words) is referenced by 11 bits lengh index).
5. Find indices of corresponding words
#### So, for the 12th word:
- 7 bits are from the remaining part of the initial **entropy**.
- 4 bits are from the checksum.
- the seed phrase lengh is `11*12=132`


- Wrap seed phrase around with some symbols to make it more visible.
- Write warning and seed phrase with delay 2 seconds.
- add entropy
## Development
### Project status
- Done. Open to feature requests.

- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow) - `main` ➕ `feature` branches. Easy to start. Good for small teams. Remember to merge often!

### Releases
Releases must follow [semantic versioning](https://semver.org/lang/uk/)  
`{major}.{minor}.{patch}-{tag}+{buildmetadata}`
-   {major} is only incremented if the release has breaking changes (includes bug fixes which have breaking behavioural changes
-   {minor} is incremented if the release has new non-breaking features
-   {patch} is incremented if the release only contains non-breaking bug fixes
- `-{tag}+{buildmetadata}**` is optional
-   {tag} denotes a **pre-release** of the version preceding. Sorting happens in ASCII sort order. For example, A-Z comes before a-z.
-   {buildmetadata} contains additional information about the version, but **does not affect** the semantic version preceding it.
- Semantic Versioning is all **about  releases, not builds**.



### Commit messages style
Use the same formatting for commit messages like [conventional commits](https://www.conventionalcommits.org/) suggests. 
```txt
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```
Following this convention, `standard-version` will be able generate `CHANGELOG.md`  automatically.
Conventional commits can be "enforced" with Husky. [Husky](https://typicode.github.io/husky/#/) is a tool for git hooks.

### Githooks
Just point git settings to existing hooks
`git config core.hooksPath .githooks`
`npm install -g @commitlint/cli @commitlint/config-conventional`

##### Linting commit messages
In this repo `.commitlintrc.yaml` is for this purpose.


## Licence
MIT License 


## Include Credits
Maxim Onishenko devops@maxim.run


Enjoy Coding ❤
