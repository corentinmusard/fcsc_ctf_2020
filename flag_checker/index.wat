(module
  (type (;0;) (func (param i32) (result i32)))
  (type (;1;) (func))
  (type (;2;) (func (param i32)))
  (type (;3;) (func (result i32)))
  (import "a" "memory" (memory (;0;) 256 256))
  (func (;0;) (type 2) (param i32)
    local.get 0
    global.set 0)
  (func (;1;) (type 0) (param i32) (result i32)
    global.get 0
    local.get 0
    i32.sub
    i32.const -16
    i32.and
    local.tee 0
    global.set 0
    local.get 0)
  (func (;2;) (type 3) (result i32)
    global.get 0)
  (func (;3;) (type 0) (param i32) (result i32)
    (local i32 i32 i32 i32 i32)
    i32.const 70
    local.set 3
    i32.const 1024
    local.set 1
    block  ;; label = @1
      local.get 0
      i32.load8_u
      local.tee 2
      i32.eqz
      br_if 0 (;@1;)
      loop  ;; label = @2
        block  ;; label = @3
          local.get 2
          local.get 1
          i32.load8_u
          local.tee 4
          i32.ne
          br_if 0 (;@3;)
          local.get 3
          i32.const -1
          i32.add
          local.tee 3
          i32.eqz
          br_if 0 (;@3;)
          local.get 4
          i32.eqz
          br_if 0 (;@3;)
          local.get 1
          i32.const 1
          i32.add
          local.set 1
          local.get 0
          i32.load8_u offset=1
          local.set 2
          local.get 0
          i32.const 1
          i32.add
          local.set 0
          local.get 2
          br_if 1 (;@2;)
          br 2 (;@1;)
        end
      end
      local.get 2
      local.set 5
    end
    local.get 5
    i32.const 255
    i32.and
    local.get 1
    i32.load8_u
    i32.sub)
  (func (;4;) (type 0) (param i32) (result i32)
    (local i32 i32)
    local.get 0
    i32.load8_u
    local.tee 2
    if  ;; label = @1
      local.get 0
      local.set 1
      loop  ;; label = @2
        local.get 1
        local.get 2
        i32.const 3
        i32.xor
        i32.store8
        local.get 1
        i32.load8_u offset=1
        local.set 2
        local.get 1
        i32.const 1
        i32.add
        local.set 1
        local.get 2
        br_if 0 (;@2;)
      end
    end
    local.get 0
    call 3
    i32.eqz)
  (func (;5;) (type 1)
    nop)
  (global (;0;) (mut i32) (i32.const 5244480))
  (export "a" (func 5))
  (export "b" (func 4))
  (export "c" (func 2))
  (export "d" (func 1))
  (export "e" (func 0))
  (data (;0;) (i32.const 1024) "E@P@x4f1g7f6ab:42`1g:f:7763133;e0e;03`6661`bee0:33fg732;b6fea44be34g0~"))
