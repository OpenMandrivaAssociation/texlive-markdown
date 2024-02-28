Name:		texlive-markdown
Version:	70117
Release:	1
Summary:	A package for converting and rendering markdown documents inside TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/markdown
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/markdown.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/markdown.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/markdown.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides facilities for the conversion of markdown
markup to plain TeX. These are provided both in form of a Lua
module and in form of plain TeX, LaTeX, and ConTeXt macro
packages that enable the direct inclusion of markdown documents
inside TeX documents. Architecturally, the package consists of
the Lunamark Lua module by John MacFarlane, which was slimmed
down and rewritten for the needs of the package. Lunamark
provides speedy markdown parsing for the rest of the package.
On top of Lunamark sits code for the plain TeX, LaTeX, and
ConTeXt formats by Vit Novotny.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/markdown
%{_texmfdistdir}/tex/luatex/markdown
%{_texmfdistdir}/tex/latex/markdown
%{_texmfdistdir}/tex/generic/markdown
%{_texmfdistdir}/tex/context/third/markdown
%{_texmfdistdir}/scripts/markdown
%doc %{_texmfdistdir}/doc/latex/markdown
%doc %{_texmfdistdir}/doc/generic/markdown
%doc %{_texmfdistdir}/doc/context/third/markdown

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
