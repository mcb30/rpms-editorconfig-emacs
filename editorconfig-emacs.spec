Name:		editorconfig-emacs
Version:	0.10.1
Release:	1%{?dist}
Summary:	EditorConfig plugin for emacs
License:	GPL-3.0-or-later
URL:		https://github.com/editorconfig/%{name}
Source0:	https://github.com/editorconfig/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:	editorconfig-init.el
BuildRequires:	emacs
BuildRequires:	texinfo
BuildArch:	noarch

%description
This is the EditorConfig plugin for emacs.  With this plugin
installed, emacs will automatically respect coding style settings
found in an .editorconfig file.

%prep
%setup -q -n %{name}-%{version}

%build

# The tarball includes an Eask file, but eask is not packaged for
# Fedora (and is unlikely to be, since it depends on multiple NPM
# modules).  Use a direct %{_emacs_bytecompile} instead.
#
%{_emacs_bytecompile} *.el

# Build info page
#
make doc/editorconfig.info

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}
install -p -m 644 *.el *.elc %{buildroot}%{_emacs_sitelispdir}/
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/
mkdir -p %{buildroot}%{_infodir}
install -p -m 644 doc/editorconfig.info %{buildroot}%{_infodir}/

%files
%doc CONTRIBUTORS CHANGELOG.md README.md
%license LICENSE
%{_emacs_sitelispdir}/editorconfig*.el
%{_emacs_sitelispdir}/editorconfig*.elc
%{_emacs_sitestartdir}/editorconfig-init.el
%{_infodir}/editorconfig*

%changelog
* Mon Feb 12 2024 Michael Brown <mbrown@fensystems.co.uk> - 0.10.1-1
- Initial package
