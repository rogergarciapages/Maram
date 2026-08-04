# Asesores Inmobiliarios MARAM SL - Landing Page

Landing page institucional y catálogo digital para **Asesores Inmobiliarios MARAM SL**, empresa especializada en la edificación de obra nueva, comercialización de desarrollos inmobiliarios y reformas integrales de alta gama en Tenerife (Islas Canarias, España).

---

## 🌟 Concepto del Proyecto

El proyecto refleja el compromiso de **MARAM SL** con la excelencia constructiva, la sostenibilidad y la cercanía en el trato al cliente under el lema *"Construimos más que edificios, construimos confianza"*. 

La plataforma está diseñada con una estética editorial moderna que acompaña al visitante en el viaje hacia la realización de su sueño de vivienda o inversión inmobiliaria en Tenerife.

### 🎨 Identidad Visual & Palette (Figma Custom Palette)
* **Red Brand Accent (`#B62B2A` / `#922222`)**: Utilizado en botones de acción principal (CTAs), navegación activa e iconos.
* **Deep Maroon & Crimson (`#190606` / `#290A0A`)**: Fondos oscuros de alta sofisticación para el Hero y el pie de página.
* **Cyan & Teal Accents (`#4af3f4` / `#2D9E9F`)**: Detalles luminosos, degradados de texto e indicadores de estado.
* **Warm Gold & Amber (`#f5b582` / `#D38C45`)**: Destacados en cifras de confianza y badges de certificación.
* **Soft Light Surfaces (`#f1f0f3` / `#fff4f0`)**: Contenedores claros con alto contraste legibilidad.

---

## 🏗️ Secciones Clave de la Plataforma

1. **Hero Principal & CTAs de Conversión**:
   * Encabezado H1 enfocado en SEO (*Obra Nueva en Tenerife: Promotora y Constructora*).
   * Botones de acción directa (*Solicitar Presupuesto* y *WhatsApp Directo* con icono SVG nativo).
2. **Barra de Indicadores de Confianza**:
   * Métricas de satisfacción, presencia insular (La Orotava y Tenerife Sur) y eficiencia energética.
3. **Sobre Nosotros & El Viaje Hacia Tu Nuevo Hogar**:
   * Historia corporativa integrada dinámicamente desde Supabase.
   * Proceso de 4 pasos (*La Ilusión Inicial*, *Tranquilidad & Plazos*, *Materiales Nobles*, *Entrega de Llaves*).
4. **Obra Nueva & Proyectos Destacados (Layout Bento Grid)**:
   * Rejilla Bento asimétrica multitono de 7 proyectos que combina filas de 2 tarjetas (8+4 / 4+8) y trípticos de 3 tarjetas (4+4+4).
5. **Servicios Inmobiliarios & Calidad Constructiva**:
   * Promotora, Constructora de Casas y Reformas Integrales.
   * **Acabados Premium**: Pavimentos porcelánicos, carpintería RPT Cortizo, baños de diseño y puertas macizas aislantes.
   * **Galería Slider**: Carrusel fotográfico interactivo con scroll suave para acabados reales.
6. **Sostenibilidad & Cumplimiento Normativo (CTE & EREE)**:
   * Sección dedicada a la eficiencia energética A+, Código Técnico de la Edificación (CTE DB-HE) y Reglamento EREE de Canarias.
7. **Contacto & Formulario Legal**:
   * Formulario con validación y casilla obligatoria RGPD de aceptación de Política de Privacidad.
8. **Pie de Página Corporativo Multi-columna**:
   * Logotipo blanco apilado verticalmente, NIF/CIF B-38974512, domicilio social en La Orotava, enlaces de servicios, aviso legal y columna dedicada a **enlaces rastreables para SEO por zonas** (Adeje, Santa Cruz, Los Cristianos, Tacoronte, San Isidro).

---

## 🛠️ Especificaciones Técnicas

* **Framework Core**: [Astro 5.x](https://astro.build/) (Modo Estático / SSG).
* **Integración CSS**: Tailwind CSS v4 mediante el plugin oficial `@tailwindcss/vite`.
* **Backend & Base de Datos**: [Supabase](https://supabase.com/) Client JS (`@supabase/supabase-javascript`) para la ingesta dinámica de datos de la empresa (`client_surveys`).
* **Tipografías**: Google Fonts — **Montserrat** (Headings) e **Inter** (Body & Labels).
* **Iconografía**: Google Material Symbols Outlined + Vectores SVG inline (WhatsApp).
* **SEO & Optimización**:
  * Esquema estructurado JSON-LD dual (`RealEstateAgent`, `GeneralContractor`).
  * Sitemap XML automático (`/sitemap.xml`).
  * Open Graph y Meta Tags enriquecidos.
  * 100% Responsive design con breakpoints para móvil, tablet y escritorio.

---

## 🚀 Comandos de Desarrollo

```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo local
astro dev --background

# Detener el servidor de desarrollo
astro dev stop

# Verificar estado y logs del dev server
astro dev status
astro dev logs

# Compilar paquete de producción estático
npm run build

# Previsualizar el build de producción localmente
npm run preview
```

---

© 2026 **Asesores Inmobiliarios MARAM SL**. Todos los derechos reservados.
