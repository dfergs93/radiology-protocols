---
title: Hosting
---

# Hosting

Protocol Manager builds to a directory of static HTML, CSS, and JavaScript files. These can be served by GitHub Pages (no server infrastructure required) or by any web server.

## Option A — GitHub Pages

GitHub Pages is the zero-infrastructure option. It is free for public repositories.

**Setup:**

1. In your forked repository on GitHub, go to **Settings → Pages**
2. Set the source to the `gh-pages` branch, root directory
3. Push any commit to `main` — the GitHub Actions workflow builds the site and pushes to `gh-pages` automatically

The workflow file is at `.github/workflows/deploy.yml`. It runs `mkdocs gh-deploy --force` on every push to `main`.

**Custom domain:**

1. Add a file named `CNAME` to `docs/` containing your custom domain (one line, no protocol):

   ```
   protocols.yourhospital.org
   ```

2. Configure a CNAME DNS record pointing your custom domain to `<your-org>.github.io`

3. In GitHub repository settings under Pages, enable HTTPS enforcement after DNS propagates

4. Update `site_url` in `mkdocs.yml` and `config/institution.yml` to your custom domain

---

## Option B — Local / Intranet Hosting

Use this option when hosting on a hospital intranet or any internal web server (nginx, Apache, IIS, or equivalent).

**Build the site:**

```bash
python scripts/generate_comparison_index.py
python scripts/generate_sitemap.py
mkdocs build
```

This writes the static site to the `site/` directory.

**Deploy:**

Copy the contents of `site/` to your web server's document root or a subdirectory. No server-side configuration is required — all files are static.

Example with nginx serving from a subdirectory:

```nginx
location /radiology/protocols/ {
    alias /var/www/radiology-protocols/;
    index index.html;
}
```

**Subdirectory base path:**

If the site is not at the root of the domain (e.g. it lives at `https://intranet.hospital.org/radiology/protocols/` rather than `https://intranet.hospital.org/`), configure the base path in two places:

In `config/institution.yml`:
```yaml
institution:
  site_url: "https://intranet.hospital.org/radiology/protocols"
  base_path: "/radiology/protocols"
```

In `mkdocs.yml`:
```yaml
site_url: https://intranet.hospital.org/radiology/protocols/
```

**Updating the site:**

Re-run the build steps above and recopy `site/` to the server whenever protocols are updated. There is no hot reload — a full rebuild and redeploy is required.
