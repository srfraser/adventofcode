defmodule FuelExTest do
  use ExUnit.Case
  doctest FuelEx

  test "greets the world" do
    assert FuelEx.hello() == :world
  end
end
