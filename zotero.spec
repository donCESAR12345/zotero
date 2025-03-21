%define debug_package %{nil}
%define __requires_exclude ^(libmozsandbox|liblgpllibs|libmozsqlite3|libmozgtk|libmozwayland|libxul|libmozavutil)\.so
%global __provides_exclude_from %{_libdir}/%{name}

Name:           zotero
Version:        7.0.9
Release:        1%{?dist}
Summary:        Zotero desktop application

License:        AGPLv3
URL:            https://www.zotero.org/
Source0:        https://download.zotero.org/client/release/%{version}/Zotero-%{version}_linux-x86_64.tar.bz2

BuildArch:      x86_64
BuildRequires:  desktop-file-utils
BuildRequires:  tar

# Use system libraries where possible
Requires:       nspr
Requires:       nss
Requires:       nss-util

Provides:       zotero

%description
Zotero is a free, easy-to-use tool to help you collect, organize, annotate, cite, and share research.

%prep
%autosetup -n Zotero_linux-x86_64

%build

%install
mkdir -p %{buildroot}{%{_bindir},%{_libdir}/%{name}}
cp -rf %{_builddir}/Zotero_linux-x86_64/* %{buildroot}%{_libdir}/%{name}/
ln -sf %{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

# Bundled .desktop file contains an overly excessive Exec line
# So we replace it with a simplified version
sed -i 's|Exec=.*|Exec=/usr/bin/zotero %U|' %{buildroot}%{_libdir}/%{name}/%{name}.desktop
# It also specifies zotero.ico as the icon, but doesn't ships the .ico, so we just use 'zotero'
sed -i 's/Icon=zotero.ico/Icon=zotero/' %{buildroot}%{_libdir}/%{name}/%{name}.desktop

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_libdir}/%{name}/%{name}.desktop

install -Dm644 %{buildroot}%{_libdir}/%{name}/icons/icon32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dm644 %{buildroot}%{_libdir}/%{name}/icons/icon64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -Dm644 %{buildroot}%{_libdir}/%{name}/icons/icon128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files
%doc
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sun Nov 17 2024 César Montoya <sprit152009@gmail.com> - 7.0.9-1
- Update to 7.0.9.
- Use bundled .desktop.
- Try to use system libraries when possible.

* Fri May 10 2024 Patrick Gaskin <patrick@pgaskin.net> - 6.0.13-4
- Rebuild.

* Sat Jul 08 2023 Patrick Gaskin <patrick@pgaskin.net> - 6.0.13-3
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 6.0.13-2
- Rebuild.

* Wed Aug 24 2022 Patrick Gaskin <patrick@pgaskin.net> - 6.0.13-1
- Update to 6.0.13.

* Sat Sep 11 2021 Patrick Gaskin <patrick@pgaskin.net> - 5.0.96.3-1
- Initial package.
