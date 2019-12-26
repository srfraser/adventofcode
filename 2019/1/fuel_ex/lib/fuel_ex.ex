defmodule FuelEx do
  @moduledoc """
  Documentation for FuelEx.
  """

  @doc """
  Hello world.

  ## Examples

      iex> FuelEx.hello()
      :world

  """
  def get_modules do
    File.stream!("../input")
    |> Stream.map(&String.trim_trailing/1)
    |> Stream.map(&String.to_integer/1)
    |> Enum.to_list()
  end


  def fuel_required(mass) do
    max(0, div(mass, 3) - 2)
  end

  def part1 do
    # frequency = List.foldl(get_modifiers(), 0, fn x, acc -> x + acc end)
    # modules = get_modules()
    total_fuel = Enum.map(get_modules(), fn x -> fuel_required(x) end)
    |> Enum.sum
    IO.puts(total_fuel)
    """
    for module <- get_modules(), into: Enum.sum do
      fuel_required(module)
    end
    """
  end

end
