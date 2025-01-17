# Licensed to Modin Development Team under one or more contributor license agreements.
# See the NOTICE file distributed with this work for additional information regarding
# copyright ownership.  The Modin Development Team licenses this file to you under the
# Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

from .arr import array

from .array_creation import (
    zeros_like,
    ones_like,
)

from .array_shaping import (
    ravel,
    shape,
    transpose,
)

from .math import (
    absolute,
    abs,
    add,
    divide,
    float_power,
    floor_divide,
    power,
    prod,
    multiply,
    remainder,
    mod,
    subtract,
    sum,
    true_divide,
    mean,
    maximum,
    amax,
    max,
    minimum,
    amin,
    min,
)

from .constants import (
    Inf,
    Infinity,
    NAN,
    NINF,
    NZERO,
    NaN,
    PINF,
    PZERO,
    e,
    euler_gamma,
    inf,
    infty,
    nan,
    newaxis,
    pi,
)


def where(condition, x=None, y=None):
    if condition is True:
        return x
    if condition is False:
        return y
    if hasattr(condition, "where"):
        return condition.where(x=x, y=y)
    raise NotImplementedError(
        f"np.where for condition of type {type(condition)} is not yet supported in Modin."
    )


__all__ = [  # noqa: F405
    "array",
    "zeros_like",
    "ones_like",
    "ravel",
    "shape",
    "transpose",
    "absolute",
    "abs",
    "add",
    "divide",
    "float_power",
    "floor_divide",
    "power",
    "prod",
    "multiply",
    "remainder",
    "mod",
    "subtract",
    "sum",
    "true_divide",
    "mean",
    "maximum",
    "amax",
    "max",
    "minimum",
    "amin",
    "min",
    "where",
    "Inf",
    "Infinity",
    "NAN",
    "NINF",
    "NZERO",
    "NaN",
    "PINF",
    "PZERO",
    "e",
    "euler_gamma",
    "inf",
    "infty",
    "nan",
    "newaxis",
    "pi",
]
