# http://github.com/russross/blackfriday
%global goipath         github.com/russross/blackfriday
%global import_path     gopkg.in/russross/blackfriday.v2
Version:                2.0.1

%global v1_import_path  gopkg.in/russross/blackfriday.v1
%global v1_version      1.5.2

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Markdown processor implemented in Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{gourl}/archive/v%{v1_version}/blackfriday-%{v1_version}.tar.gz
Source2:        glide.yaml
Source3:        glide.lock

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%package v2-devel
Summary:       %{summary}
BuildArch:     noarch

%description v2-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%autosetup -n blackfriday-%{v1_version} -T -b 1
%forgesetup
cp %{SOURCE2} %{SOURCE3} .


%install
%goinstall glide.yaml glide.lock
%goinstall -i %{import_path} -o devel.file-list

cw=$(pwd)
cd ../blackfriday-%{v1_version}
%goinstall -i %{v1_import_path} -o ${cw}/v1_devel.file-list


%check
%gochecks
pushd %{buildroot}/%{gopath}/src/%{import_path}/
%gochecks -i %{import_path}
popd
pushd %{buildroot}/%{gopath}/src/%{v1_import_path}/
%gochecks -i %{v1_import_path}
popd

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f v1_devel.file-list
%license LICENSE.txt
%doc README.md

%files v2-devel -f devel.file-list
%license LICENSE.txt
%doc README.md

%changelog
* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-2
- Install both v1 and v2 version

* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-1
- Update to release 2.0.1

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 2.0.0-4.20180215git55d61fa
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3.git55d61fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 2.0.0-2.git55d61fa
- Upload glide files

* Thu Mar 01 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.0-1.20180215git55d61fa
- Bump to upstream 55d61fa8aa702f59229e6cff85793c22e580eaf5

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com>
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.5-1
- Update to v1.5
  related: #1222338

* Wed Aug 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.2-20
- Bump to upstream 0ba0f2b6ed7c475a92e4df8641825cb7a11d1fa3
  related: #1222338

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.2-17
- Bump to upstream 5f33e7b7878355cd2b7e6b8eefc48a5472c69f70
  related: #1222338

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 1.2-14
- Bump to upstream 300106c228d52c8941d4b3de6054a6062a86dda3
  related: #1222338

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 1.2-13
- Bump to upstream 8cec3a854e68dba10faabbe31c089abf4a3e57a6
  related: #1222338

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2-10
- Change deps on compiler(go-compiler)
- Update Arches
- Use %%license

* Tue Aug 25 2015 jchaloup <jchaloup@redhat.com> - 1.2-9
- Provide devel package on rhel7
  related: #1222338

* Wed Aug 12 2015 Fridolin Pokorny <fpokorny@redhat.com> - 1.2-8
- Update spec file to spec-2.0
  related: #1222338

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 jchaloup <jchaloup@redhat.com> - 1.2-6
- Add license macro for LICENSE
- Remove runtime dependency on golang.
  resolves: #1222338

* Mon Mar 02 2015 jchaloup <jchaloup@redhat.com> - 1.2-5
- Bump to upstream 77efab57b2f74dd3f9051c79752b2e8995c8b789
  Update spec file to used commit tarball
  related: #1156176

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 1.2-4
- Add commit and shortcommit global variable
  related: #1156176

* Fri Oct 31 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2-3
- include fedora/rhel arch conditionals

* Mon Oct 27 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2-2
- runtime requires go.net/html

* Fri Oct 24 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2-1
- Resolves: rhbz#1156176 - Initial package
