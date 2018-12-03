defmodule Day1Ex do
  @moduledoc """
  Documentation for Day1Ex.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Day1Ex.hello()
      :world

  """
  def get_modifiers do
    File.stream!("../input")
    |> Stream.map(&String.trim_trailing/1)
    |> Stream.map(&String.to_integer/1)
    |> Enum.to_list()
  end

  def part1 do
    frequency = List.foldl(get_modifiers(), 0, fn x, acc -> x + acc end)
    IO.puts(frequency)
  end

  def part2 do
    result =
      Enum.reduce_while(Stream.cycle(get_modifiers()), {MapSet.new([0]), 0}, fn x, acc ->
        next = elem(acc, 1) + x

        if MapSet.member?(elem(acc, 0), next),
          do: {:halt, next},
          else: {:cont, {MapSet.put(elem(acc, 0), next), next}}
      end)

    IO.puts(result)
  end
end
