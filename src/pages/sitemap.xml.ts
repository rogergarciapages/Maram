export async function GET() {
	const siteUrl = 'https://ventos-construction.com';
	
	const pages = [
		{ url: '', changefreq: 'weekly', priority: 1.0 },
		{ url: '/encuesta', changefreq: 'monthly', priority: 0.8 },
		{ url: '/proyectos', changefreq: 'daily', priority: 0.9 },
		{ url: '/contacto', changefreq: 'monthly', priority: 0.8 },
	];

	const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.map(page => `  <url>
    <loc>${siteUrl}${page.url}</loc>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${page.priority}</priority>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
  </url>`).join('\n')}
</urlset>`;

	return new Response(sitemap, {
		headers: {
			'Content-Type': 'application/xml',
			'Cache-Control': 'public, max-age=86400',
		},
	});
}