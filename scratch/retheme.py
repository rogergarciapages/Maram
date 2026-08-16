import re

input_path = r"c:\Projects\ventos-astro-viewer\src\pages\index.astro"
output_path = r"c:\Projects\ventos-astro-viewer\src\pages\index.astro"

with open(input_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace specific legacy color hex codes and Tailwind classes with the new 3-color palette:
# Dark Charcoal Slate: #343B43
# Light Cream: #F1EDE0
# Off White: #FAF9F6

replacements = [
    # 1. Body & Nav
    ('class="bg-[#f1f0f3] text-[#1e1d29] selection:bg-[#B62B2A] selection:text-white"',
     'class="bg-[#FAF9F6] text-[#343B43] selection:bg-[#343B43] selection:text-[#FAF9F6]"'),
    
    ('class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-[#ceced6] text-[#1e1d29] shadow-sm"',
     'class="fixed top-0 w-full z-50 bg-[#FAF9F6]/95 backdrop-blur-md border-b border-[#F1EDE0] text-[#343B43] shadow-sm"'),
    
    ('text-[#1e1d29]', 'text-[#343B43]'),
    ('text-[#B62B2A]', 'text-[#343B43]'),
    ('border-[#B62B2A]', 'border-[#343B43]'),
    ('text-[#5e5c76]', 'text-[#343B43]/80'),
    ('hover:text-[#B62B2A]', 'hover:text-[#343B43]'),
    ('shadow-[#B62B2A]/30', 'shadow-[#343B43]/20'),
    ('shadow-[#B62B2A]/40', 'shadow-black/30'),
    ('shadow-[#B62B2A]/20', 'shadow-[#343B43]/20'),
    ('shadow-[#2D9E9F]/20', 'shadow-[#343B43]/20'),
    ('shadow-[#D38C45]/20', 'shadow-[#343B43]/20'),
    
    # Hero Section
    ('bg-[#190606]', 'bg-[#252A30]'),
    ('bg-[#2D9E9F]/20 border border-[#4af3f4]/40 text-[#4af3f4]',
     'bg-[#F1EDE0]/20 border border-[#F1EDE0]/40 text-[#F1EDE0]'),
    ('bg-[#4af3f4]', 'bg-[#F1EDE0]'),
    ('text-[#ceced6]', 'text-[#FAF9F6]/80'),
    ('bg-[#1e1d29]/80 border border-[#2D9E9F]/50 text-white px-8 py-4 text-[12px] uppercase tracking-[0.1em] font-bold hover:bg-[#2D9E9F]/20 backdrop-blur-md transition-all flex items-center justify-center gap-2 rounded',
     'bg-[#343B43]/90 border border-[#F1EDE0]/50 text-[#FAF9F6] px-8 py-4 text-[12px] uppercase tracking-[0.1em] font-bold hover:bg-[#F1EDE0]/20 backdrop-blur-md transition-all flex items-center justify-center gap-2 rounded'),
    ('fill-[#4af3f4]', 'fill-[#F1EDE0]'),

    # Trust Bar & Dark Sections
    ('bg-[#1e1d29]', 'bg-[#343B43]'),
    ('border-[#2D9E9F]/30', 'border-[#F1EDE0]/20'),
    ('divide-[#5e5c76]/40', 'divide-[#F1EDE0]/20'),
    
    # About Section
    ('border-[#ceced6]', 'border-[#F1EDE0]'),
    ('bg-[#ceced6]', 'bg-[#F1EDE0]'),
    ('text-[#3D3B4F]', 'text-[#343B43]/90'),
    ('bg-[#B62B2A]/10 text-[#B62B2A] text-[11px] font-bold uppercase tracking-wider border border-[#B62B2A]/20',
     'bg-[#F1EDE0] text-[#343B43] text-[11px] font-bold uppercase tracking-wider border border-[#343B43]/20'),
    ('hover:border-[#B62B2A]', 'hover:border-[#343B43]'),
    ('hover:border-[#2D9E9F]', 'hover:border-[#343B43]'),
    ('hover:border-[#D38C45]', 'hover:border-[#343B43]'),
    ('hover:text-[#2D9E9F]', 'hover:text-[#343B43]'),
    ('hover:text-[#D38C45]', 'hover:text-[#343B43]'),

    # Bento Grid
    ('text-[#4af3f4]', 'text-[#F1EDE0]'),
    ('border-[#2D9E9F]/40', 'border-[#F1EDE0]/30'),
    ('from-[#190606]/95 via-[#190606]/30 to-transparent', 'from-[#252A30]/95 via-[#252A30]/40 to-transparent'),
    ('bg-[#1e1d29]/90 text-[#4af3f4] text-[10px] font-bold px-3 py-1 uppercase tracking-wider border border-[#2D9E9F]/50 rounded',
     'bg-[#343B43]/90 text-[#F1EDE0] text-[10px] font-bold px-3 py-1 uppercase tracking-wider border border-[#F1EDE0]/40 rounded'),
    ('bg-[#1e1d29]/90 text-[#f5b582] text-[10px] font-bold px-3 py-1 uppercase tracking-wider border border-[#D38C45]/50 rounded',
     'bg-[#343B43]/90 text-[#FAF9F6] text-[10px] font-bold px-3 py-1 uppercase tracking-wider border border-[#F1EDE0]/40 rounded'),
    ('border-[#4af3f4]', 'border-[#F1EDE0]'),
    ('hover:text-[#4af3f4]', 'hover:text-[#F1EDE0]'),
    ('border-[#f5b582]', 'border-[#F1EDE0]'),
    ('hover:text-[#f5b582]', 'hover:text-[#F1EDE0]'),

    # Services Section
    ('bg-[#f1f0f3]', 'bg-[#FAF9F6]'),
    ('bg-[#2D9E9F]/10 rounded-xl flex items-center justify-center text-[#2D9E9F] group-hover:bg-[#2D9E9F] group-hover:text-white transition-all',
     'bg-[#F1EDE0] rounded-xl flex items-center justify-center text-[#343B43] group-hover:bg-[#343B43] group-hover:text-[#FAF9F6] transition-all'),
    ('bg-[#B62B2A]/10 rounded-xl flex items-center justify-center text-[#B62B2A] group-hover:bg-[#B62B2A] group-hover:text-white transition-all',
     'bg-[#F1EDE0] rounded-xl flex items-center justify-center text-[#343B43] group-hover:bg-[#343B43] group-hover:text-[#FAF9F6] transition-all'),
    ('bg-[#D38C45]/10 rounded-xl flex items-center justify-center text-[#D38C45] group-hover:bg-[#D38C45] group-hover:text-white transition-all',
     'bg-[#F1EDE0] rounded-xl flex items-center justify-center text-[#343B43] group-hover:bg-[#343B43] group-hover:text-[#FAF9F6] transition-all'),
    ('bg-[#2D9E9F]', 'bg-[#343B43]'),
    ('bg-[#D38C45]', 'bg-[#343B43]'),
    ('bg-[#486A7F]', 'bg-[#343B43]'),
    
    # Finishes & Eco Sections
    ('bg-[#D38C45]/10 rounded-lg flex items-center justify-center text-[#D38C45]',
     'bg-[#F1EDE0] rounded-lg flex items-center justify-center text-[#343B43]'),
    ('bg-[#2D9E9F]/10 rounded-lg flex items-center justify-center text-[#2D9E9F]',
     'bg-[#F1EDE0] rounded-lg flex items-center justify-center text-[#343B43]'),
    ('bg-[#B62B2A]/10 rounded-lg flex items-center justify-center text-[#B62B2A]',
     'bg-[#F1EDE0] rounded-lg flex items-center justify-center text-[#343B43]'),
    ('bg-[#486A7F]/10 rounded-lg flex items-center justify-center text-[#486A7F]',
     'bg-[#F1EDE0] rounded-lg flex items-center justify-center text-[#343B43]'),
    ('hover:bg-[#B62B2A] hover:text-white hover:border-[#B62B2A]',
     'hover:bg-[#343B43] hover:text-[#FAF9F6] hover:border-[#343B43]'),
    ('text-[#f5b582]', 'text-[#F1EDE0]'),

    # Eco section
    ('bg-[#2D9E9F]/10 text-[#2D9E9F] text-[11px] font-bold uppercase tracking-wider border border-[#2D9E9F]/30',
     'bg-[#343B43]/10 text-[#343B43] text-[11px] font-bold uppercase tracking-wider border border-[#343B43]/20'),
    ('bg-[#2D9E9F]/10 rounded flex items-center justify-center text-[#2D9E9F]',
     'bg-[#F1EDE0] rounded flex items-center justify-center text-[#343B43]'),
    ('bg-[#D38C45]/10 rounded flex items-center justify-center text-[#D38C45]',
     'bg-[#F1EDE0] rounded flex items-center justify-center text-[#343B43]'),
    ('bg-[#B62B2A]/10 rounded flex items-center justify-center text-[#B62B2A]',
     'bg-[#F1EDE0] rounded flex items-center justify-center text-[#343B43]'),
    ('bg-[#486A7F]/10 rounded flex items-center justify-center text-[#486A7F]',
     'bg-[#F1EDE0] rounded flex items-center justify-center text-[#343B43]'),

    # Local expertise & Contact form
    ('bg-[#3D3B4F]', 'bg-[#252A30]'),
    ('bg-[#fbe6db] border-t border-[#D38C45]/30',
     'bg-[#F1EDE0] border-t border-[#343B43]/20'),
    ('focus:border-[#B62B2A]', 'focus:border-[#343B43]'),
    ('text-[#B62B2A] underline font-medium hover:text-[#922222]',
     'text-[#343B43] underline font-medium hover:text-[#252A30]'),
    ('accent-[#B62B2A]', 'accent-[#343B43]'),
    ('focus:ring-[#B62B2A]', 'focus:ring-[#343B43]'),
    
    # Footer
    ('border-[#5e5c76]/30', 'border-[#F1EDE0]/20'),
    ('text-[#ceced6]/70', 'text-[#FAF9F6]/60'),
    ('text-[#ceced6]/80', 'text-[#FAF9F6]/70'),
]

for old, new in replacements:
    content = content.replace(old, new)

# Also replace hero overlay in CSS block
css_old = '''.hero-overlay {
				background: linear-gradient(
					135deg,
					rgba(25, 6, 6, 0.92) 0%,
					rgba(41, 10, 10, 0.75) 50%,
					rgba(30, 29, 41, 0.85) 100%
				);
			}'''

css_new = '''.hero-overlay {
				background: linear-gradient(
					135deg,
					rgba(52, 59, 67, 0.94) 0%,
					rgba(37, 42, 48, 0.82) 50%,
					rgba(28, 32, 36, 0.92) 100%
				);
			}'''

content = content.replace(css_old, css_new)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Retheming transformation script completed successfully.")
