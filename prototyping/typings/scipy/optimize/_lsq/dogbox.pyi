"""
This type stub file was generated by pyright.
"""

"""
Dogleg algorithm with rectangular trust regions for least-squares minimization.

The description of the algorithm can be found in [Voglis]_. The algorithm does
trust-region iterations, but the shape of trust regions is rectangular as
opposed to conventional elliptical. The intersection of a trust region and
an initial feasible region is again some rectangle. Thus, on each iteration a
bound-constrained quadratic optimization problem is solved.

A quadratic problem is solved by well-known dogleg approach, where the
function is minimized along piecewise-linear "dogleg" path [NumOpt]_,
Chapter 4. If Jacobian is not rank-deficient then the function is decreasing
along this path, and optimization amounts to simply following along this
path as long as a point stays within the bounds. A constrained Cauchy step
(along the anti-gradient) is considered for safety in rank deficient cases,
in this situations the convergence might be slow.

If during iterations some variable hit the initial bound and the component
of anti-gradient points outside the feasible region, then a next dogleg step
won't make any progress. At this state such variables satisfy first-order
optimality conditions and they are excluded before computing a next dogleg
step.

Gauss-Newton step can be computed exactly by `numpy.linalg.lstsq` (for dense
Jacobian matrices) or by iterative procedure `scipy.sparse.linalg.lsmr` (for
dense and sparse matrices, or Jacobian being LinearOperator). The second
option allows to solve very large problems (up to couple of millions of
residuals on a regular PC), provided the Jacobian matrix is sufficiently
sparse. But note that dogbox is not very good for solving problems with
large number of constraints, because of variables exclusion-inclusion on each
iteration (a required number of function evaluations might be high or accuracy
of a solution will be poor), thus its large-scale usage is probably limited
to unconstrained problems.

References
----------
.. [Voglis] C. Voglis and I. E. Lagaris, "A Rectangular Trust Region Dogleg
            Approach for Unconstrained and Bound Constrained Nonlinear
            Optimization", WSEAS International Conference on Applied
            Mathematics, Corfu, Greece, 2004.
.. [NumOpt] J. Nocedal and S. J. Wright, "Numerical optimization, 2nd edition".
"""
def lsmr_operator(Jop, d, active_set): # -> LinearOperator:
    """Compute LinearOperator to use in LSMR by dogbox algorithm.

    `active_set` mask is used to excluded active variables from computations
    of matrix-vector products.
    """
    ...

def find_intersection(x, tr_bounds, lb, ub): # -> tuple[Any, Any, Any, Any, Any, Any]:
    """Find intersection of trust-region bounds and initial bounds.

    Returns
    -------
    lb_total, ub_total : ndarray with shape of x
        Lower and upper bounds of the intersection region.
    orig_l, orig_u : ndarray of bool with shape of x
        True means that an original bound is taken as a corresponding bound
        in the intersection region.
    tr_l, tr_u : ndarray of bool with shape of x
        True means that a trust-region bound is taken as a corresponding bound
        in the intersection region.
    """
    ...

def dogleg_step(x, newton_step, g, a, b, tr_bounds, lb, ub): # -> tuple[Unknown, NDArray[Any], Literal[False]] | tuple[Unknown, NDArray[Any], bool_]:
    """Find dogleg step in a rectangular region.

    Returns
    -------
    step : ndarray, shape (n,)
        Computed dogleg step.
    bound_hits : ndarray of int, shape (n,)
        Each component shows whether a corresponding variable hits the
        initial bound after the step is taken:
            *  0 - a variable doesn't hit the bound.
            * -1 - lower bound is hit.
            *  1 - upper bound is hit.
    tr_hit : bool
        Whether the step hit the boundary of the trust-region.
    """
    ...

def dogbox(fun, jac, x0, f0, J0, lb, ub, ftol, xtol, gtol, max_nfev, x_scale, loss_function, tr_solver, tr_options, verbose):
    ...

