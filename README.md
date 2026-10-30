# Sergei Voronov — Portfolio

Independent static portfolio migrated from Framer. Two routes: `/` and `/projects/`.

## Local development

Requires Node.js 22 or newer. No packages to install.

```sh
npm run build
npm run dev
```

Open http://127.0.0.1:4173. Re-run the build after editing source files.

- `src/projects.mjs`: project descriptions, contributions, tags and links.
- `src/styles.css`: shared design and responsive layouts.
- `scripts/build.mjs`: page templates and static generation.
- `assets/`: local copies of original portfolio media.
- `dist/`: generated output (not tracked).

## GitHub Pages

The included workflow builds and deploys both pages when pushed to `main`, or when manually started. In the repository's Settings → Pages select **GitHub Actions** as the source. Relative paths support both a repository subdirectory and a custom domain. Publication has not yet been performed.

The CV link still points to the existing Google Drive document. CV revision is deferred.
