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
- `src/ru.mjs`: Russian project translations and tag labels.
- `src/app.js`: persistent RU/ENG switch and viewport-based video playback.
- `src/styles.css`: shared design and responsive layouts.
- `scripts/build.mjs`: page templates and static generation.
- `assets/`: local copies of original portfolio media.
- `dist/`: generated output (not tracked).

## GitHub Pages

The included workflow builds and deploys both pages when pushed to `main`, or when manually started. In the repository's Settings → Pages select **GitHub Actions** as the source. Relative paths support both a repository subdirectory and a custom domain. Publication has not yet been performed.

The CV link still points to the existing Google Drive document. CV revision is deferred.

## Languages and media

Both pages include English and Russian content. RU/ENG switches the entire page, document title and accessibility labels. The selection is saved in localStorage and carried in navigation URLs (`?lang=ru` / `?lang=en`), including when storage is unavailable. Proper names remain unchanged. The linked CV remains the existing document.

Cards use local muted looping MP4 with JPEG posters. Videos load only when visible and pause outside the viewport or in a background tab. Reduced-motion preferences show still posters. GIFs are excluded from the deployment output.
