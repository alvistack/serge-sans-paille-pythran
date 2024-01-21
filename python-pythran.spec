# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pythran
Epoch: 100
Version: 0.13.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Ahead of Time compiler for numeric kernels
License: BSD-3-Clause
URL: https://github.com/serge-sans-paille/pythran/tags
Source0: %{name}_%{version}.orig.tar.gz
Source99: %{name}.rpmlintrc
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-beniget >= 0.4.0
BuildRequires: python3-devel
BuildRequires: python3-gast >= 0.5.0
BuildRequires: python3-numpy
BuildRequires: python3-ply >= 3.4
BuildRequires: python3-setuptools

%description
Pythran is an ahead of time compiler for a subset of the Python
language, with a focus on scientific computing. It takes a Python module
annotated with a few interface descriptions and turns it into a native
Python module with the same interface, but (hopefully) faster.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pythran
Summary: Ahead of Time compiler for numeric kernels
Requires: python3
Requires: python3-beniget >= 0.4.0
Requires: python3-gast >= 0.5.0
Requires: python3-numpy
Requires: python3-ply >= 3.4
Provides: python3-pythran = %{epoch}:%{version}-%{release}
Provides: python3dist(pythran) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pythran = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pythran) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pythran = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pythran) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pythran
Pythran is an ahead of time compiler for a subset of the Python
language, with a focus on scientific computing. It takes a Python module
annotated with a few interface descriptions and turns it into a native
Python module with the same interface, but (hopefully) faster.

%files -n python%{python3_version_nodots}-pythran
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-pythran
Summary: Ahead of Time compiler for numeric kernels
Requires: python3
Requires: python3-beniget >= 0.4.0
Requires: python3-gast >= 0.5.0
Requires: python3-numpy
Requires: python3-ply >= 3.4
Provides: python3-pythran = %{epoch}:%{version}-%{release}
Provides: python3dist(pythran) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pythran = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pythran) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pythran = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pythran) = %{epoch}:%{version}-%{release}

%description -n python3-pythran
Pythran is an ahead of time compiler for a subset of the Python
language, with a focus on scientific computing. It takes a Python module
annotated with a few interface descriptions and turns it into a native
Python module with the same interface, but (hopefully) faster.

%files -n python3-pythran
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-pythran
Summary: Ahead of Time compiler for numeric kernels
Requires: python3
Requires: python3-beniget >= 0.4.0
Requires: python3-gast >= 0.5.0
Requires: python3-numpy
Requires: python3-ply >= 3.4
Provides: python3-pythran = %{epoch}:%{version}-%{release}
Provides: python3dist(pythran) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pythran = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pythran) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pythran = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pythran) = %{epoch}:%{version}-%{release}

%description -n python3-pythran
Pythran is an ahead of time compiler for a subset of the Python
language, with a focus on scientific computing. It takes a Python module
annotated with a few interface descriptions and turns it into a native
Python module with the same interface, but (hopefully) faster.

%files -n python3-pythran
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
