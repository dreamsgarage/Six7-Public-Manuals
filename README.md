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

`MANIFEST.json` names the repository, the commit and the SHA-256 of every manual page in the edition. The Core Operator manual is Six7's own and is never published here.

The pages link to each other by file name, so they must stay side by side in the root of the repository.

## Publishing a new edition

1. Merge the manual changes in each app's repository first.
2. Collect the pages from local checkouts of the six repositories, all in one folder (each checkout is fetched, never changed):

   ```sh
   tools/collect.sh ~/Work/Six7
   ```

3. Update the edition date in `index.html` (hero and footer), and any size shown on the landing page that changed.
4. Open `index.html` locally and check every link.
5. Commit, tag the edition (`manuals-YYYY-MM-DD`) and push. Pages serves `main` a minute or so later.

To go back to an earlier edition, restore its tag onto `main` and push.

## Search engines

The landing page asks search engines not to list it (`noindex`). The manual pages don't carry that tag (they are built in the app repositories), and a project site can't have its own `robots.txt`, so a search engine that finds a link to a manual elsewhere may list it. Anyone with the link can read every page.

Google Workspace is a trademark of Google LLC. Six7 is not affiliated with Google.
