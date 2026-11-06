# Six7 public manuals

The published edition of the Six7 customer manuals, served by GitHub Pages:
**https://dreamsgarage.github.io/Six7-Public-Manuals/**

This repository holds built pages only. The manuals are written and built in each app's own (private) repository, under `docs/manual/`. Nothing here changes when those repositories change: an edition is a frozen copy, and it changes only when someone publishes a new one.

## What is published

| Page | Manual | Built in |
|---|---|---|
| `index.html` | Landing page (the six7.work light theme) | this repository |
| `six7-suite.html` | Suite manual | Six7 |
| `six7-hub-user.html` | Hub User manual | Six7-Core |
| `six7-crm-configuration.html`, `six7-crm-user.html` | CRM | SIX7-CRM |
| `six7-kanban-configuration.html`, `six7-kanban-user.html` | Kanban | SIX7-Kanban |
| `six7-service-desk-configuration.html`, `six7-service-desk-user.html` | Service Desk | SIX7-Service-Desk |
| `six7-contracts-providers-configuration.html`, `six7-contracts-providers-user.html` | Contracts & Providers | SIX7-Contracts-Providers |

`MANIFEST.json` names, for every manual page in the edition, the repository and commit it was built at, the SHA-256 of the page as built there (`source_sha256`) and of the page as published here (`sha256`). The Core Operator manual is Six7's own and is never published here.

## Credits added here

Every published manual closes with the collaboration credits, as six7.work does: "A collaboration we like.", the Claude, Omarchy and Entangled Forge logos (linked to anthropic.com/claude, omarchy.org and Entangled Forge's [Both-and](https://www.entangledforge.com/en/perspectives/both-and/) perspective) and a link to [six7.work](https://six7.work/). `tools/credits.py` adds them while the pages are collected, from the logos in `assets/credits/`. **The manuals in the app repositories don't have them and are not changed:** the credits belong to this public edition only. The landing page has the same block as its section 03.

The pages link to each other by file name, so they must stay side by side in the root of the repository.

## Publishing a new edition

1. Merge the manual changes in each app's repository first.
2. Collect the pages from local checkouts of the six repositories, all in one folder (each checkout is fetched, never changed). The script adds the credits to each page:

   ```sh
   tools/collect.sh ~/Work/Six7
   ```

3. Update the edition in `index.html` (hero and footer), every size shown on the landing page, and `lastmod` in `sitemap.xml`.
4. Open `index.html` locally and check every link.
5. Commit, tag the edition (`manuals-YYYY-MM-DD`) and push. Pages serves `main` a minute or so later.

To go back to an earlier edition, restore its tag onto `main` and push.

## Search engines

The edition is open to search engines: the landing page has a canonical address, and `sitemap.xml` lists it and the ten manuals. A project site can't have its own `robots.txt`, so submit `https://dreamsgarage.github.io/Six7-Public-Manuals/sitemap.xml` in Google Search Console and Bing Webmaster Tools to have it read.

Google Workspace is a trademark of Google LLC. Six7 is not affiliated with Google.
