(defmacro nullify (varname) `(setf ,varname nil))

;; (defvar foo 4)
;; (nullify foo)
;; foo
;; pass by value

(defun testfun (x y)
  (+ x y))
