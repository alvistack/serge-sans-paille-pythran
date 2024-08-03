#ifndef PYTHONIC_INCLUDE_DISPATCH_SORT_HPP
#define PYTHONIC_INCLUDE_DISPATCH_SORT_HPP

#include "pythonic/include/builtins/list/sort.hpp"
#include "pythonic/include/numpy/sort.hpp"

PYTHONIC_NS_BEGIN

namespace __dispatch__
{

  template <class T, class... Args>
  auto sort(types::list<T> &l, Args &&...args)
      -> decltype(pythonic::builtins::list::sort(l,
                                                 std::forward<Args>(args)...));
  template <class T, class... Args>
  auto sort(types::list<T> &&l, Args &&...args)
      -> decltype(pythonic::builtins::list::sort(std::move(l),
                                                 std::forward<Args>(args)...));
  template <class Any, class... Args>
  types::none_type sort(Any &&any, Args &&...args);

  DEFINE_FUNCTOR(pythonic::__dispatch__, sort);
} // namespace __dispatch__
PYTHONIC_NS_END

#endif
